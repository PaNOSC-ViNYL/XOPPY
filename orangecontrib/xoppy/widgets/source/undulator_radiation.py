import sys

from PyQt4.QtGui import QIntValidator, QDoubleValidator, QApplication
from orangewidget import gui
from orangewidget.settings import Setting
from oasys.widgets import gui as oasysgui, congruence
from oasys.widgets.exchange import DataExchangeObject
from collections import OrderedDict
from orangecontrib.xoppy.widgets.gui.ow_xoppy_widget import XoppyWidget
from orangecontrib.xoppy.util import srundplug

import scipy.constants as codata
codata_mee = codata.codata.physical_constants["electron mass energy equivalent in MeV"][0]

class OWundulator_radiation(XoppyWidget):
    name = "Undulator Radiation"
    id = "orange.widgets.dataundulator_radiation"
    description = "xoppy application to compute UNDULATOR RADIATION"
    icon = "icons/xoppy_undulator_radiation.png"
    priority = 4
    category = ""
    keywords = ["xoppy", "undulator_radiation"]

    ELECTRONENERGY = Setting(6.04)
    ELECTRONENERGYSPREAD = Setting(0.001)
    ELECTRONCURRENT = Setting(0.2)
    ELECTRONBEAMSIZEH = Setting(0.000395)
    ELECTRONBEAMSIZEV = Setting(9.9e-06)
    ELECTRONBEAMDIVERGENCEH = Setting(1.05e-05)
    ELECTRONBEAMDIVERGENCEV = Setting(3.9e-06)
    PERIODID = Setting(0.018)
    NPERIODS = Setting(222)
    KV = Setting(1.68)
    DISTANCE = Setting(30.0)
    GAPH = Setting(0.003)
    GAPV = Setting(0.003)
    HSLITPOINTS = Setting(41)
    VSLITPOINTS = Setting(41)
    METHOD = Setting(0)

    def build_gui(self):

        box = oasysgui.widgetBox(self.controlArea, self.name + " Input Parameters", orientation="vertical", width=self.CONTROL_AREA_WIDTH-5)
        
        idx = -1 
        
        #widget index 0 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONENERGY",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 1 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONENERGYSPREAD",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 2 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONCURRENT",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 3 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONBEAMSIZEH",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 4 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONBEAMSIZEV",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 5 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONBEAMDIVERGENCEH",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 6 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "ELECTRONBEAMDIVERGENCEV",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 7 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "PERIODID",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 8 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "NPERIODS",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=int, validator=QIntValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 9 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "KV",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 10 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "DISTANCE",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 11 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "GAPH",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 12 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "GAPV",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=float, validator=QDoubleValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 13 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "HSLITPOINTS",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=int, validator=QIntValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 14 
        idx += 1 
        box1 = gui.widgetBox(box) 
        oasysgui.lineEdit(box1, self, "VSLITPOINTS",
                     label=self.unitLabels()[idx], addSpace=False,
                    valueType=int, validator=QIntValidator(), orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 15 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.comboBox(box1, self, "METHOD",
                     label=self.unitLabels()[idx], addSpace=False,
                    items=['US', 'URGENT', 'SRW','pySRU'],
                    valueType=int, orientation="horizontal", labelWidth=250)
        self.show_at(self.unitFlags()[idx], box1) 

    def unitLabels(self):
         return ["Electron Energy [GeV]", "Electron Energy Spread", "Electron Current [A]", "Electron Beam Size H [m]", "Electron Beam Size V [m]", "Electron Beam Divergence H [rad]", "Electron Beam Divergence V [rad]", "Period ID [m]", "Number of periods", "Kv [undulator K value vertical field]", "Distance to slit [m]", "Slit gap H [m]", "Slit gap V [m]", "Number of slit mesh points in H", "Number of slit mesh points in V", "calculation code"]

    def unitFlags(self):
         return ["True", "self.METHOD != 1", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True"]

    def get_help_name(self):
        return 'undulator_radiation'

    def check_fields(self):
        self.ELECTRONENERGY = congruence.checkStrictlyPositiveNumber(self.ELECTRONENERGY, "Electron Energy")
        if not self.METHOD == 1: self.ELECTRONENERGYSPREAD = congruence.checkPositiveNumber(self.ELECTRONENERGYSPREAD, "Electron Energy Spread")
        self.ELECTRONCURRENT = congruence.checkStrictlyPositiveNumber(self.ELECTRONCURRENT, "Electron Current")
        self.ELECTRONBEAMSIZEH = congruence.checkPositiveNumber(self.ELECTRONBEAMSIZEH, "Electron Beam Size H")
        self.ELECTRONBEAMSIZEV = congruence.checkPositiveNumber(self.ELECTRONBEAMSIZEV, "Electron Beam Size V")
        self.ELECTRONBEAMDIVERGENCEH = congruence.checkPositiveNumber(self.ELECTRONBEAMDIVERGENCEH, "Electron Beam Divergence H")
        self.ELECTRONBEAMDIVERGENCEV = congruence.checkPositiveNumber(self.ELECTRONBEAMDIVERGENCEV, "Electron Beam Divergence V")
        self.PERIODID = congruence.checkStrictlyPositiveNumber(self.PERIODID, "Period ID")
        self.NPERIODS = congruence.checkStrictlyPositiveNumber(self.NPERIODS, "Number of Periods")
        self.KV = congruence.checkPositiveNumber(self.KV, "Kv")
        self.DISTANCE = congruence.checkPositiveNumber(self.DISTANCE, "Distance to slit")
        self.GAPH = congruence.checkPositiveNumber(self.GAPH, "Slit gap H")
        self.GAPV = congruence.checkPositiveNumber(self.GAPV, "Slit gap V")
        self.HSLITPOINTS = congruence.checkStrictlyPositiveNumber(self.HSLITPOINTS, "Number of slit mesh points in H")
        self.VSLITPOINTS = congruence.checkStrictlyPositiveNumber(self.VSLITPOINTS, "Number of slit mesh points in V")

        if sys.platform == 'linux' and self.METHOD == 2:
            raise Exception("SRW calculation code not supported under Linux")


    def plot_results(self, calculated_data, progressBarValue=80):
        if not self.view_type == 0:
            if not calculated_data is None:
                self.view_type_combo.setEnabled(False)

                data = calculated_data.get_content("xoppy_data")
                code = calculated_data.get_content("xoppy_code")

                h = data[0]
                v = data[1]
                p = data[2]

                try:
                    print(">>>>> Result shapes",h.shape,v.shape,p[0].shape )

                    self.plot_data2D(p[0], h, v, 0, 0,
                                     xtitle='H [mm]',
                                     ytitle='V [mm]',
                                     title='Code '+code+'; Flux [photons/s/0.1%bw/mm^2]')

                    self.tabs.setCurrentIndex(0)
                except Exception as e:
                    self.view_type_combo.setEnabled(True)

                    raise Exception("Data not plottable: bad content\n" + str(e))

                self.view_type_combo.setEnabled(True)
            else:
                raise Exception("Empty Data")

    def do_xoppy_calculation(self):
        return xoppy_calc_undulator_radiation(ELECTRONENERGY=self.ELECTRONENERGY,ELECTRONENERGYSPREAD=self.ELECTRONENERGYSPREAD,ELECTRONCURRENT=self.ELECTRONCURRENT,ELECTRONBEAMSIZEH=self.ELECTRONBEAMSIZEH,ELECTRONBEAMSIZEV=self.ELECTRONBEAMSIZEV,ELECTRONBEAMDIVERGENCEH=self.ELECTRONBEAMDIVERGENCEH,ELECTRONBEAMDIVERGENCEV=self.ELECTRONBEAMDIVERGENCEV,PERIODID=self.PERIODID,NPERIODS=self.NPERIODS,KV=self.KV,DISTANCE=self.DISTANCE,GAPH=self.GAPH,GAPV=self.GAPV,HSLITPOINTS=self.HSLITPOINTS,VSLITPOINTS=self.VSLITPOINTS,METHOD=self.METHOD)

    def extract_data_from_xoppy_output(self, calculation_output):
        e, h, v, p, code = calculation_output

        calculated_data = DataExchangeObject("XOPPY", self.get_data_exchange_widget_name())

        calculated_data.add_content("xoppy_data", [h, v, p])
        calculated_data.add_content("xoppy_code", code)

        return calculated_data


    def get_data_exchange_widget_name(self):
        return "UNDULATOR_RADIATION"

    def getTitles(self):
        return ['Undulator Flux']

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

def xoppy_calc_undulator_radiation(ELECTRONENERGY=6.04,ELECTRONENERGYSPREAD=0.001,ELECTRONCURRENT=0.2,\
                                       ELECTRONBEAMSIZEH=0.000395,ELECTRONBEAMSIZEV=9.9e-06,\
                                       ELECTRONBEAMDIVERGENCEH=1.05e-05,ELECTRONBEAMDIVERGENCEV=3.9e-06,\
                                       PERIODID=0.018,NPERIODS=222,KV=1.68,DISTANCE=30.0,GAPH=0.003,GAPV=0.003,\
                                       HSLITPOINTS=41,VSLITPOINTS=41,METHOD=0):
    print("Inside xoppy_calc_undulator_radiation. ")

    bl = OrderedDict()
    bl['ElectronBeamDivergenceH'] = ELECTRONBEAMDIVERGENCEH
    bl['ElectronBeamDivergenceV'] = ELECTRONBEAMDIVERGENCEV
    bl['ElectronBeamSizeH'] = ELECTRONBEAMSIZEH
    bl['ElectronBeamSizeV'] = ELECTRONBEAMSIZEV
    bl['ElectronCurrent'] = ELECTRONCURRENT
    bl['ElectronEnergy'] = ELECTRONENERGY
    bl['ElectronEnergySpread'] = ELECTRONENERGYSPREAD
    bl['Kv'] = KV
    bl['NPeriods'] = NPERIODS
    bl['PeriodID'] = PERIODID
    bl['distance'] = DISTANCE
    bl['gapH'] = GAPH
    bl['gapV'] = GAPV


    gamma = ELECTRONENERGY / (codata_mee * 1e-3)
    print ("Gamma: %f \n"%(gamma))

    resonance_wavelength = (1 + bl['Kv']**2 / 2.0) / 2 / gamma**2 * bl["PeriodID"]
    m2ev = codata.c * codata.h / codata.e      # lambda(m)  = m2eV / energy(eV)
    resonance_energy = m2ev / resonance_wavelength

    print ("Resonance wavelength [A]: %g \n"%(1e10*resonance_wavelength))
    print ("Resonance energy [eV]: %g \n"%(resonance_energy))

    energy = None
    if energy == None:
        energy = resonance_energy

    #TODO SPEC file can be removed
    outFile = "undulator_radiation.spec"

    # Memorandum:
    # e = array with energy in eV
    # h = array with horizontal positions in mm
    # v = array with vertical positions in mm
    # p = array with photon flux in photons/s/0.1%bw/mm^2 with shape (Ne,Nh.Nv)
    if METHOD == 0:
        code = "US"
        print("Undulator radiation calculation using US. Please wait...")
        e,h,v,p = srundplug.calc3d_us(bl,fileName=outFile,fileAppend=False,hSlitPoints=HSLITPOINTS,vSlitPoints=VSLITPOINTS,
                                    photonEnergyMin=energy,photonEnergyMax=13000,photonEnergyPoints=1,zero_emittance=False)
        print("Done")
    if METHOD == 1:
        code = "URGENT"
        print("Undulator radiation calculation using URGENT. Please wait...")
        e,h,v,p = srundplug.calc3d_urgent(bl,fileName=outFile,fileAppend=False,hSlitPoints=HSLITPOINTS,vSlitPoints=VSLITPOINTS,
                                    photonEnergyMin=energy,photonEnergyMax=13000,photonEnergyPoints=1,zero_emittance=False)
        print("Done")
    if METHOD == 2:
        code = "SRW"
        print("Undulator radiation calculation using SRW. Please wait...")
        e,h,v,p = srundplug.calc3d_srw(bl,fileName=outFile,fileAppend=False,hSlitPoints=HSLITPOINTS,vSlitPoints=VSLITPOINTS,
                                    photonEnergyMin=energy,photonEnergyMax=13000,photonEnergyPoints=1,zero_emittance=False)
        print("Done")
    if METHOD == 3:
        code = "pySRU"
        print("Undulator radiation calculation using SRW. Please wait...")
        e,h,v,p = srundplug.calc3d_pysru(bl,fileName=outFile,fileAppend=False,hSlitPoints=HSLITPOINTS,vSlitPoints=VSLITPOINTS,
                                    photonEnergyMin=energy,photonEnergyMax=13000,photonEnergyPoints=1,zero_emittance=False)
        print("Done")

    return e, h, v, p, code



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OWundulator_radiation()
    w.show()
    app.exec()
    w.saveSettings()