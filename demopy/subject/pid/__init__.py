class PID:
    def __init__(self, KP, KI, KD, E0, integral_filtering=True):
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.E0 = E0
        self.EV = [E0]
        # for I-part
        self.integral_filtering = integral_filtering
        self.SI = 0

    def progress(self):
        KP = self.KP
        KI = self.KI
        KD = self.KD
        EV = self.EV

        # P
        SP = KP * EV[-1]

        # I
        self.integral()
        SI = self.SI
        SI *= KI

        # D
        if len(self.EV) == 1:
            SD = 0
        else:
            SD = KD * (EV[-1] - EV[-2])

        DU = SP + SI + SD
        # todo remove debug
        print("%16f = %16f, %16f, %16f, %s" % (DU, SP, SI, SD, self.integral_filtering))
        E = EV[-1] + DU
        # fix value
        E = self.fix(E)
        # go ahead
        EV.append(E)
        return E

    def integral(self):
        if self.integral_filtering:
            self.integral_filter()
        else:
            self.SI += self.EV[-1]

    def integral_filter(self):
        E0 = self.E0

        I = self.EV[-1]
        if self.integral_filtering:
            if (I < 0 and E0 < 0) or (I > 0 and E0 > 0):
                # just ignore I part
                return 0
            else:
                self.integral_filtering = False
        self.SI += I

    def __next__(self):
        return self.progress()

    def fix(self, E):
        return E
