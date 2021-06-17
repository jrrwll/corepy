class PID_S:

    def __init__(self, KP, KI, KD, T, U0, U):
        """
        PID Control System
        :param KP, constant P of PID
        :param KI, constant I of PID
        :param KD, constant D of PID
        :param T, the calculation cycle
        :param U0, initial value
        :param U, target value
        """
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.T = T
        self.U0 = U0
        self.U = U
        self.UV = [U0]
        self.k = 1
        self.error = U0 - U
        self.error_1 = U0 - U
        self.error_2 = U0 - U

    def __next__(self):
        KP = self.KP
        KI = self.KI
        KD = self.KD
        T = self.T
        UV = self.UV
        U = self.U
        k = self.k

        error = self.error
        error_1 = self.error_1
        error_2 = self.error_2

        # UV[k]
        UK = UV[k - 1] + (KP + KI * T + KD / T) * error + (KP + 2 * KD / T) * error_1 + KD / T * error_2
        # update status
        UV.append(UK)
        self.k += 1
        self.error_2 = error_1
        self.error_1 = error
        self.error = UK - U
        return UK

    def progress(self):
        return self.__next__()
