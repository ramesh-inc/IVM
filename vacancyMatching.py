from dbModule import sq_vacancies as vacClass, sq_nb_prediction as nbpClass, sq_dt_prediction as dtpClass, sq_vacancy_matching as vmClass

class VacancyMatching:
    def __init__(self):
        self.vac = vacClass.sq_vacancies()
        self.vm = vmClass.sq_vacancy_matching()
        self.nbp = nbpClass.sq_nb_prediction()
        self.dtp = dtpClass.sq_dt_prediction()

    def resultFormat(self, jobTitle, precentage):
        return str(jobTitle) + ' - ' + str(precentage) + '%'

    def updateMatching(self, jobId, userId, nbVal, dtVal):
        if self.vm.getCountId(jobId, userId) == 0:
            self.vm.setCvForJobVacancy(jobId, userId, nbVal, dtVal)

    def matchingByUserId(self, userid):
        nbResult = self.nbp.getMatchingByUserId(userid)
        dtResult = self.dtp.getMatchingByUserId(userid)
        nbVal = self.resultFormat(nbResult[0], nbResult[1])
        dtVal = self.resultFormat(dtResult[0], dtResult[1])

        for vacency in self.vac.getLiveVacenciesByName(nbResult[0]):
            self.updateMatching(vacency[0], userid, nbVal, dtVal)

    def matchingByVacencyId(self, vacencyId):
        vacResult = self.vac.getLiveVacenciesById(vacencyId)

        for res in self.nbp.getMatchingByJob(vacResult[1]):
            dtpResult = self.dtp.getMatchingByUserId(res[0])
            nbVal = self.resultFormat(res[1], res[2])
            dtVal = self.resultFormat(dtpResult[0], dtpResult[1])

            self.updateMatching(vacResult[0], res[0], nbVal, dtVal)

if __name__ == "__main__":
    vm = VacancyMatching()
    vm.matchingByVacencyId(24)