# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canale_view.ui'
#
# Created: Wed Apr 08 21:55:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_facewindow(object):
    def setupUi(self, facewindow):
        facewindow.setObjectName(_fromUtf8("facewindow"))
        facewindow.resize(1230, 568)
        facewindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../git/SiMPlE/smfsmanager/D_mica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        facewindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(facewindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter_4 = QtGui.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget = QtGui.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.grafo = PlotWidget(self.layoutWidget)
        self.grafo.setMinimumSize(QtCore.QSize(600, 0))
        self.grafo.setToolTip(_fromUtf8(""))
        self.grafo.setStatusTip(_fromUtf8(""))
        self.grafo.setWhatsThis(_fromUtf8(""))
        self.grafo.setObjectName(_fromUtf8("grafo"))
        self.verticalLayout_2.addWidget(self.grafo)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radio_deriv = QtGui.QRadioButton(self.layoutWidget)
        self.radio_deriv.setObjectName(_fromUtf8("radio_deriv"))
        self.horizontalLayout.addWidget(self.radio_deriv)
        self.radio_view = QtGui.QRadioButton(self.layoutWidget)
        self.radio_view.setChecked(True)
        self.radio_view.setObjectName(_fromUtf8("radio_view"))
        self.horizontalLayout.addWidget(self.radio_view)
        self.radio_smooth = QtGui.QRadioButton(self.layoutWidget)
        self.radio_smooth.setObjectName(_fromUtf8("radio_smooth"))
        self.horizontalLayout.addWidget(self.radio_smooth)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labDetails = QtGui.QLabel(self.layoutWidget)
        self.labDetails.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labDetails.setObjectName(_fromUtf8("labDetails"))
        self.horizontalLayout_3.addWidget(self.labDetails)
        self.labFilename = QtGui.QLabel(self.layoutWidget)
        self.labFilename.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labFilename.setObjectName(_fromUtf8("labFilename"))
        self.horizontalLayout_3.addWidget(self.labFilename)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.layoutWidget1 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_3 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.formLayoutWidget = QtGui.QWidget(self.splitter_3)
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("border: none;"))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.s_mth = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.s_mth.setFont(font)
        self.s_mth.setStyleSheet(_fromUtf8("border: none;"))
        self.s_mth.setDecimals(3)
        self.s_mth.setMaximum(1000.0)
        self.s_mth.setSingleStep(0.1)
        self.s_mth.setProperty("value", 3.0)
        self.s_mth.setObjectName(_fromUtf8("s_mth"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.s_mth)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("border: none;"))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.s_vth = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.s_vth.setFont(font)
        self.s_vth.setStyleSheet(_fromUtf8("border: none;"))
        self.s_vth.setMaximum(9999.0)
        self.s_vth.setSingleStep(0.1)
        self.s_vth.setProperty("value", 10.0)
        self.s_vth.setObjectName(_fromUtf8("s_vth"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.s_vth)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("border: none;"))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.sg_fw = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.sg_fw.setFont(font)
        self.sg_fw.setStyleSheet(_fromUtf8("border: none;"))
        self.sg_fw.setMinimum(0.01)
        self.sg_fw.setMaximum(99.99)
        self.sg_fw.setSingleStep(0.1)
        self.sg_fw.setProperty("value", 1.0)
        self.sg_fw.setObjectName(_fromUtf8("sg_fw"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sg_fw)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("border: none;"))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.sg_mm = QtGui.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.sg_mm.setFont(font)
        self.sg_mm.setStyleSheet(_fromUtf8("border: none;"))
        self.sg_mm.setMinimum(0)
        self.sg_mm.setMaximum(90)
        self.sg_mm.setProperty("value", 10)
        self.sg_mm.setObjectName(_fromUtf8("sg_mm"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sg_mm)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("border: none;"))
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.plath = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.plath.setFont(font)
        self.plath.setMinimum(-100000.0)
        self.plath.setMaximum(100000.0)
        self.plath.setProperty("value", 30.0)
        self.plath.setObjectName(_fromUtf8("plath"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.plath)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("border: none;"))
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lasth = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.lasth.setFont(font)
        self.lasth.setMaximum(1000.0)
        self.lasth.setProperty("value", 5.0)
        self.lasth.setObjectName(_fromUtf8("lasth"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lasth)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("border: none;"))
        self.label_7.setLineWidth(1)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.derorder = QtGui.QSpinBox(self.formLayoutWidget)
        self.derorder.setMaximum(10)
        self.derorder.setProperty("value", 1)
        self.derorder.setObjectName(_fromUtf8("derorder"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.derorder)
        self.pjlist = QtGui.QListWidget(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.pjlist.setFont(font)
        self.pjlist.setStyleSheet(_fromUtf8(""))
        self.pjlist.setObjectName(_fromUtf8("pjlist"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.splitter_3)
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.sslabel = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.sslabel.setFont(font)
        self.sslabel.setStyleSheet(_fromUtf8("border: none;"))
        self.sslabel.setTextFormat(QtCore.Qt.AutoText)
        self.sslabel.setObjectName(_fromUtf8("sslabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.sslabel)
        self.lcd_Tposition = QtGui.QLCDNumber(self.formLayoutWidget_3)
        self.lcd_Tposition.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_Tposition.setNumDigits(6)
        self.lcd_Tposition.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Tposition.setProperty("value", 100000.0)
        self.lcd_Tposition.setObjectName(_fromUtf8("lcd_Tposition"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lcd_Tposition)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("border: none;"))
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lcd_Tlength = QtGui.QLCDNumber(self.formLayoutWidget_3)
        self.lcd_Tlength.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_Tlength.setNumDigits(6)
        self.lcd_Tlength.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Tlength.setObjectName(_fromUtf8("lcd_Tlength"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lcd_Tlength)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("border: none;"))
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lcd_Tstep = QtGui.QLCDNumber(self.formLayoutWidget_3)
        self.lcd_Tstep.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_Tstep.setNumDigits(6)
        self.lcd_Tstep.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Tstep.setObjectName(_fromUtf8("lcd_Tstep"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lcd_Tstep)
        self.label_16 = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("border: none;"))
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lcd_Tslope = QtGui.QLCDNumber(self.formLayoutWidget_3)
        self.lcd_Tslope.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_Tslope.setNumDigits(5)
        self.lcd_Tslope.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Tslope.setObjectName(_fromUtf8("lcd_Tslope"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lcd_Tslope)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pj_p = QtGui.QRadioButton(self.formLayoutWidget_3)
        self.pj_p.setEnabled(False)
        self.pj_p.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pj_p.setCheckable(True)
        self.pj_p.setChecked(True)
        self.pj_p.setObjectName(_fromUtf8("pj_p"))
        self.horizontalLayout_2.addWidget(self.pj_p)
        self.pj_j = QtGui.QRadioButton(self.formLayoutWidget_3)
        self.pj_j.setEnabled(False)
        self.pj_j.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pj_j.setObjectName(_fromUtf8("pj_j"))
        self.horizontalLayout_2.addWidget(self.pj_j)
        self.formLayout_3.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.sslabel_2 = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.sslabel_2.setFont(font)
        self.sslabel_2.setStyleSheet(_fromUtf8("border: none;"))
        self.sslabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.sslabel_2.setObjectName(_fromUtf8("sslabel_2"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.sslabel_2)
        self.fil_io = QtGui.QProgressBar(self.formLayoutWidget_3)
        self.fil_io.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fil_io.setMaximum(1)
        self.fil_io.setProperty("value", 1)
        self.fil_io.setTextVisible(False)
        self.fil_io.setObjectName(_fromUtf8("fil_io"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.fil_io)
        self.label_17 = QtGui.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("border: none;"))
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_17)
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("border: none;"))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lcd_N = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.lcd_N.setNumDigits(3)
        self.lcd_N.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_N.setObjectName(_fromUtf8("lcd_N"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lcd_N)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("border: none;"))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lcd_Np = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.lcd_Np.setNumDigits(3)
        self.lcd_Np.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Np.setObjectName(_fromUtf8("lcd_Np"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lcd_Np)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("border: none;"))
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lcd_Nj = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.lcd_Nj.setNumDigits(3)
        self.lcd_Nj.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Nj.setObjectName(_fromUtf8("lcd_Nj"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lcd_Nj)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("border: none;"))
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lcd_Nblue = QtGui.QLCDNumber(self.formLayoutWidget_2)
        self.lcd_Nblue.setNumDigits(3)
        self.lcd_Nblue.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Nblue.setObjectName(_fromUtf8("lcd_Nblue"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lcd_Nblue)
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bAddFile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bAddFile.setObjectName(_fromUtf8("bAddFile"))
        self.verticalLayout.addWidget(self.bAddFile)
        self.bAddFiles = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bAddFiles.setObjectName(_fromUtf8("bAddFiles"))
        self.verticalLayout.addWidget(self.bAddFiles)
        self.bAddDir = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bAddDir.setObjectName(_fromUtf8("bAddDir"))
        self.verticalLayout.addWidget(self.bAddDir)
        self.bReset = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bReset.setObjectName(_fromUtf8("bReset"))
        self.verticalLayout.addWidget(self.bReset)
        self.bDoSave = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bDoSave.setObjectName(_fromUtf8("bDoSave"))
        self.verticalLayout.addWidget(self.bDoSave)
        self.mainlist = QtGui.QListWidget(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        self.mainlist.setFont(font)
        self.mainlist.setObjectName(_fromUtf8("mainlist"))
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.horizontalLayout_4.addWidget(self.splitter_4)
        facewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(facewindow)
        QtCore.QMetaObject.connectSlotsByName(facewindow)

    def retranslateUi(self, facewindow):
        facewindow.setWindowTitle(_translate("facewindow", "MainWindow", None))
        self.radio_deriv.setText(_translate("facewindow", "Derivative", None))
        self.radio_view.setText(_translate("facewindow", "Curve", None))
        self.radio_smooth.setText(_translate("facewindow", "Smooth", None))
        self.labDetails.setText(_translate("facewindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">xxx</p></body></html>", None))
        self.labFilename.setText(_translate("facewindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">FILENAME</span></p></body></html>", None))
        self.label.setText(_translate("facewindow", "Thresh (std)", None))
        self.label_2.setText(_translate("facewindow", "MinLen [nm]", None))
        self.label_3.setText(_translate("facewindow", "Window", None))
        self.label_4.setText(_translate("facewindow", "Slope (°)", None))
        self.label_5.setText(_translate("facewindow", "Zdist [nm]", None))
        self.label_6.setText(_translate("facewindow", "LastTH [pN]", None))
        self.label_7.setText(_translate("facewindow", "TraitsOrder", None))
        self.sslabel.setText(_translate("facewindow", "Position", None))
        self.label_14.setText(_translate("facewindow", "Length", None))
        self.label_15.setText(_translate("facewindow", "Step size", None))
        self.label_16.setText(_translate("facewindow", "Slope", None))
        self.pj_p.setText(_translate("facewindow", "P", None))
        self.pj_j.setText(_translate("facewindow", "J", None))
        self.sslabel_2.setText(_translate("facewindow", "Accept", None))
        self.label_17.setText(_translate("facewindow", "Type", None))
        self.label_8.setText(_translate("facewindow", "N", None))
        self.label_9.setText(_translate("facewindow", "N-plateaux", None))
        self.label_10.setText(_translate("facewindow", "N-jumps", None))
        self.label_11.setText(_translate("facewindow", "N-out", None))
        self.bAddFile.setText(_translate("facewindow", "Load one file", None))
        self.bAddFiles.setText(_translate("facewindow", "Load Files", None))
        self.bAddDir.setText(_translate("facewindow", "Load DIR", None))
        self.bReset.setText(_translate("facewindow", "Reset", None))
        self.bDoSave.setText(_translate("facewindow", "Do stats and save", None))

from pyqtgraph import PlotWidget
