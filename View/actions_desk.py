class ViewDesk:
    def show_desk(self, Yabc, X, func):  # 10*10
        first = "%5s|" % ("")
        for i in Yabc:
            first = first + '%5s|' % (str(i))
        s = first + '\n'
        for x in X:
            s = s + '%5d|' % x
            for y in Yabc:
                s = s + "%5s|" % (func.get(str(x) + "," + str(y)))
            s = s + "\n"

        return s