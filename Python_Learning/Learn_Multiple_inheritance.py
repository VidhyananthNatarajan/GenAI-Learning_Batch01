class SBI_Bank:

    def roi_sbi_homeloan(self):
        print("The rate of interest is 8.5%")

class Indian_Bank:

    def roi_ind_homeloan(self):
        print("The rate of interest is 8.78%")        

class roi_bank(SBI_Bank,Indian_Bank):
    
    def roi_homeloan(self):
        print("The rate of interest is 9.0%")

obj01 = roi_bank()

obj01.roi_homeloan()
obj01.roi_ind_homeloan()
obj01.roi_sbi_homeloan()     