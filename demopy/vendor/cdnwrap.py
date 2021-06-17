from qiniu import Auth, put_file, etag
from qiniu import CdnManager

from retrying import retry


class QiniuWrapper:
    def __init__(self, access_key, secret_key):
        self.auth = Auth(access_key, secret_key)
        self.cdn_manager = CdnManager(self.auth)

    @retry(wait_fixed=3000, stop_max_attempt_number=3)
    def upload(self, bucket_name, key, local_file):
        """
        上传
        :param bucket_name: 空间
        :param key: 上传后保存的文件名
        :param local_file: 要上传文件的本地路径
        :return:
        """

        # 生成上传 Token
        token = self.auth.upload_token(bucket_name, key)
        ret, info = put_file(token, key, local_file)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(local_file)

    def refresh(self, urls: list):
        refresh_url_result = self.cdn_manager.refresh_urls(urls)
        print(refresh_url_result)


import upyun


class UpyunWrapper:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_service(self, service, timeout=15, endpoint=upyun.ED_AUTO):
        """
        注册服务名，用于upyun.UpYun对象的重用
        :param service: bucket
        :param timeout:
        :param endpoint:
        :return:
        """
        self[service] = upyun.UpYun(
            service, self.username, self.password,
            timeout=timeout, endpoint=endpoint)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    @retry(wait_fixed=3000, stop_max_attempt_number=3)
    def upload(self, service: upyun.UpYun, key, localfile, headers=None):
        with open(localfile, 'rb') as f:
            res = service.put(key=key, value=f, checksum=True, headers=headers)
            print(res)

    @staticmethod
    def refresh(service: upyun.UpYun, urls: list, domain=None):
        res = service.purge(keys=urls, domain=domain)
        for i in res:
            print(i)
