import re
import datetime as dt

class text_modification:

    def convertString(self, obj):
        """convert variable to string

            Args:
               obj : any type of a value (int,double,float,...)
            Return:
                string
        """
        return ''.join(obj)


    def removeUnicode(self, obj):
        """remove unicode characters from given string

            Args:
               obj : string
            Return:
                string
        """
        return (obj.encode('ascii', 'ignore')).decode("utf-8")


    def stripString(self, obj):
        """remove both leading and trailing characters of string

            Args:
               obj : string
            Return:
                string
        """
        return obj.strip()


    def splitContent(self, obj, symbol):
        """split string according to given special character

            Args:
               obj : string
               symbol : special character
            Return:
                string
        """
        return obj.split(symbol)


    def splitStringBySpace(self, obj):
        """split string by the space

            Args:
               obj : string
            Return:
                string
        """
        return obj.split()


    def filterIntegers(self, obj):
        """get only integer from a string

            Args:
               obj : string
            Return:
                Array, including only integer values of given string
        """
        return [int(s) for s in re.findall(r'-?\d+\.?\d*', obj)]


    def stringLowercase(self, obj):
        """Convert any kind of string to lowercase sting
            Args:
               obj : string

            Return:
                string
        """
        return obj.lower()


    def stringUppercase(self, obj):
        """Convert any kind of string to uppercase sting
            Args:
               obj : string

            Return:
                string
        """
        return obj.upper()


    def datetimeToUnix(self, year, month, date):
        """Convert a date to UNIX timestamp format

            Args:
               year : Year of the date
               month : Month of the date
               date : Date of the date
            Return:
                date from UNIX timestamp format
        """
        return int(dt.datetime(int(year), int(month), int(date)).timestamp())


    def unixToDatetime(self, obj):
        """Convert UNIX timestamp format date into datetime variable

            Args:
               obj : UNIX timestamp format date
            Return:
                date from datetime format
        """
        return dt.datetime.fromtimestamp(int(obj))


    def monthFind(self, month):
        """get the number related to month

            Args:
                month : name of the month
            Return:
                number related to month (int)
        """
        varList = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
        return varList[self.stringLowercase(str(month))]


    def timeFromat(self, time, source):
        """filter date from the given source and convert into UNIX timestamp format

            Args:
                month : string, include the date and other characters
            Return:
                date from UNIX timestamp format
        """
        if source == 'adaderana_biztop':
            varList = self.splitStringBySpace(time)
            varList[0] = varList[0].replace(',', '')
            varList[1] = varList[1].replace(',', '')

            return self.datetimeToUnix(varList[2],self.monthFind(varList[0]),varList[1])

        elif source == 'itn_localnews':
            varList = self.splitStringBySpace(time)
            varList[0] = self.monthFind(self.stringLowercase(varList[0]))
            varList[1] = varList[1].replace(',', '')
            return self.datetimeToUnix(varList[2], varList[0], varList[1])

        else:
            return self.datetimeToUnix(time.year, time.month, time.day)