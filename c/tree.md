# Model tree

Type
- A Atrial
- V Ventricular
- P Purkinje
- S SA node
- N AV node
- e embryonic stem cell
- i induced pluripotent stem cell

Species
- C Canine
- F Frog
- G Guinea pig
- H Human
- L Rat
- M Mouse
- P Pig
- R Rabbit
- m Mammal

Recording type
- f recordings in fibres or multicellular preparations, instead of isolated cells

Models are included if they represent the dynamics of a single cell or, for early models, of a small, space-clamped, multicellular preparation.
Models are omitted if they contain spatial propagation, either in larger tissues or by dividing the cell into a multitude of "calcium release units".
(The above holds only for this overview file. The repository on the whole contains models of other cell types, models of single currents, and more.)

Whether or not a modification counts as a "model" is entirely subjective.
No strict criteria are used here, I just tried to make it useful.

## 1962 Noble mPf
Base: HH1952
| [Paper](https://doi.org/10.1113/jphysiol.1962.sp006849) Noble (1962) A Modification of the Hodgkin-Huxley Equations Applicable to Purkinje Fibre Action and Pacemaker Potentials

## 1966 Krause
Krause, Antoni, Fleckenstein (1966) An electronic model for the formation of local and transmitted stimuli on the myocardium fibers based upon variable current-voltage characteristics for potassium and sodium ions

Note: In german. Can't find it online

## 1975 McAllister HPf
Base: [Noble 1962](#1962-noble-mpf)
| [Paper](https://doi.org/10.1113/jphysiol.1975.sp011080) McAllister, Noble, Tsien (1975) Reconstruction of the electrical activity of cardiac Purkinje fibres

Known as: McAllister-Noble-Tsien (MNT)

## Beeler 1977 mVf
**Included**
| Base: [McAllister 1975](#1975-mcallister-hpf)
| [Paper](https://doi.org/10.1113/jphysiol.1977.sp011853) Beeler, Reuter (1977) Reconstruction of the action potential of ventricular myocardial fibres

Known as: Beeler-Reuter (BR)

Modifications:
- Adds INa j gate based on work w. Haas
- ...

## 1980 Yanagihara mSf
Base: Mixed
| [Paper](https://doi.org/10.2170/jjphysiol.30.841) Yanagihara, Noma, Irisawa (1980) Reconstruction of sino-atrial node pacemaker potential based on the voltage clamp experiments

## 1982 Bristow rSf
Base: [McAllister 1975](#1975-mcallister-hpf)
| [Paper](https://doi.org/10.1152/ajpheart.1982.243.2.h207) Bristow, Clark (1982) A mathematical model of primary pacemaking cell in SA node of the heart

Known as: Bristow-Clark

## 1982 Irisawa rSf
Base: [Yanagihara 1980](#1980-yanagihara-msf)
| [Chapter](https://doi.org/10.1007/978-94-009-7535-4_4) Irisawa, Noma (1982) Pacemaker mechanisms of rabbit sinoatrial node cells, in: Bouman, Jongsma (Eds.), Cardiac Rate and Rhythm: Physiological, Morphological, and Developmental Aspects

Known as: Irisawa-Noma

## 1984 Noble mSf
Base: [DiFrancesco 1985](#1985-difrancesco-mpf)
| [Paper](https://doi.org/10.1098/rspb.1984.0065) Noble, Noble (1984) A model of sino-atrial node electrical activity based on a modification of the DiFrancesco-Noble 1984 equations

Known as: Noble-Noble model

Note: This is an adaptation of the DiFrancesco 1985 model, but was published earlier. It cites DiFrancesco 1985 as "1984 (in the press)".

## 1985 DiFrancesco mPf
Base: [McAllister 1975](#1975-mcallister-hpf)
[Paper](https://doi.org/10.1098/rstb.1985.0001) DiFrancesco, Noble (1985) A Model of the Cardiac Electrical Activity Incorporating Ionic Pumps and Concentration Changes

Known as: DiFrancesco-Noble model

Bits:
- INaK new formulation

## 1985 Reiner rSf
Base: [Bristow 1982](#1982-bristow-rsf)
| [Paper](https://doi.org/10.1152/ajpheart.1985.249.6.h1143) Reiner, Antzelevitch (1985) Phase resetting and annihilation in a mathematical model of sinus node

Known as: Reiner-Antzelevitch

## 1987 Drouhard
Base: [Beeler 1977](#1977-beeler-mvf)
| [Paper](https://doi.org/10.1016/0010-4809(87)90048-6) Drouhard, Roberge (1987) Revised formulation of the Hodgkin-Huxley representation of the sodium current in cardiac cells

Known as: Drouhard-Roberge, BRDR

Modifications:
- Remove INa j gate again

## 1987 Hilgemann RAf
Base: [DiFrancesco 1985](#1985-difrancesco-mpf)
| [Paper](https://doi.org/10.1098/rspb.1987.0015) Hilgemann, Noble (1987) Excitation-contraction coupling and extracellular calcium transients in rabbit atrium; reconstruction of basic cellular mechanisms

## 1989 Noble mS
Chapter: "DiFrancesco, Noble, Denyer (1989) Ionic Mechanisms in Normal and Abnormal Cardiac Pacemaker Activity", in "Jacklet (Ed, 1989) Neuronal and Cellular Oscillators".

Known as: Noble-DiFrancesco-Denyer

## 1990 Earm RA
Base: [Hilgemann 1987](#1987-hilgemann-raf)
| Code for this paper is inside "Oxsoft Heart"
| [Paper](https://doi.org/10.1098/rspb.1990.0028) Earm, Noble (1990) A model of the single atrial cell; relation between calcium current and calcium release

## 1990a Rasmusson FS
[Paper](https://doi.org/10.1152/ajpheart.1990.259.2.h352) Rasmusson, Clark et al., Campbell (1990) A mathematical model of a bullfrog cardiac pacemaker cell

## 1990b Rasmusson FA
[Paper](https://doi.org/10.1152/ajpheart.1990.259.2.h370) Rasmusson, Clark et al., Campbell (1990) A mathematical model of electrophysiological activity in a bullfrog atrial cell

## 1991 Luo GV
Base: [Beeler 1977](#1977-beeler-mvf)
| [*Updated* Matlab code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/01.res.68.6.1501) Luo, Rudy (1991) A model of the ventricular cardiac action potential. Depolarization, repolarization, and their interaction.

Known as: Luo-Rudy model, LR1, Luo-Rudy phase 1 model

Bits:
- INa based on Ebihara 1980, but with a j gate added back in

## 1991 Noble GV
Base: [Earm 1990](#1990-earm-ra)
| Code for this paper is inside "Oxsoft Heart"
| [Paper]() Noble, Noble et al., So (1991) The Role of Sodium-Calcium Exchange During the Cardiac Action Potential

## 1991 Wilders mS
Base: [Noble 1984](#1984-noble-msf)
| [Paper](https://doi.org/10.1016/s0006-3495(91)82155-5) Wilders, Jongsma, Van Ginneken (1991) Pacemaker activity of the rabbit sinoatrial node; A comparison of mathematical models

## 1993 Karma mV

## 1993 Nordin GV
[Paper](https://doi.org/10.1152/ajpheart.1993.265.6.H2117) Nordin (1993) Computer model of membrane current and intracellular Ca2 flux in the isolated guinea pig ventricular myocyte
**Has erratum**

Bits:
- INaK new formulation

## 1993 Winslow
## 1994 Demir RS

## 1994 Luo GV
Base: [Luo 1991](#1991-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.74.6.1071) Luo, Rudy (1994) A dynamic model of the cardiac ventricular action potential I; Simulations of ionic currents and concentration changes

Known as: LRd, LR2, Luo-Rudy phase 2 model

Modifications:
- INaK new formulation
- Rescaled gK1
- ...

## 1995 Zeng GV
Base: [1994 Luo GV](#1994-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.77.1.140) Zeng, Laurita, Rosenbaum, Rudy (1995) Two Components of the Delayed Rectifier K Current in Ventricular Myocytes of the Guinea Pig Type

Modifications:
- Splits IK into IKr and IKs
- Calcium buffering, with an analytical solution to a higher-order problem that ends up involving arccos and cos.
- ...

## 1996 Dokos RS

## 1996 Lindblad RA
Base: Mostly new?
| [Paper](https://doi.org/10.1152/ajpheart.1996.271.4.h1666) Lindblad, Murphey, Clark Giles (1996) A model of the action potential and underlying membrane currents in a rabbit atrial cell

## 1997 Endresen mS

## 1998 Courtemanche HA
**Included**
| Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1152/ajpheart.1998.275.1.h301) Courtemanche, Ramirez, Nattel (1998) Ionic mechanisms underlying human atrial action potential properties; insights from a mathematical model

## 1998 Espinosa LV
## 1998 Fenton mV

## 1998 Jafri GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1016/s0006-3495(98)77832-4) Jafri, Rice, Winslow (1998) Cardiac Ca2 Dynamics; The Roles of Ryanodine Receptor Adaptation and Sarcoplasmic Reticulum Load

## 1998 Noble GV

## 1998 Nygren HA
**Included**
| Base: [Lindblad 1996](#1996-lindblad-ra)
| [Paper](https://doi.org/10.1161/01.res.82.1.63) Nygren, Fiset et al., Giles (1998) Mathematical model of an adult human atrial cell; the role of K-currents in repolarization

## 1998 Priebe HV
**Included**
| Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.82.11.1206) Priebe, Beuckelmann (1998) Simulation study of cellular electric properties in heart failure

## 1998 Riemer GV
## 1999 Demir RS
## 1999 Dumaine GV
## 1999 Irvine INA Include?
## 1999 Rice GV
## 1999 Viswanathan GV

## 1999 Winslow CV
Base: [Jafri 1998](#1998-jafri-gv)
| [Paper](https://doi.org/10.1161/01.res.84.5.571) Winslow, Rice et al., O'Rourke (1999) Mechanisms of Altered Excitation-Contraction Coupling in Canine Tachycardia-Induced Heart Failure, II Model Studies

## 2000 Faber GV
[Original code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/s0006-3495(00)76783-x) Faber, Rudy (2000) Action Potential and Contractility in [Na+]i Overloaded Cardiac Myocytes

## 2000 Greenstein CV

## 2000 Ramirez CA
Base: [Courtemanche 1998](#1998-courtemanche-ha)
| [Paper](https://doi.org/10.1152/ajpheart.2000.279.4.h1767) Ramirez, Nattel, Courtemanche (2000) Mathematical analysis of canine atrial action potentials; rate, regional factors, and electrical remodeling

## 2000 Sakmann GV

## 2000 Zhang RS
[Paper](https://doi.org/10.1152/ajpheart.2000.279.1.h397) Zhang, Holden et al., Boyett (2000) Mathematical models of action potentials in the periphery and center of the rabbit sinoatrial node

## 2001 Boyett
## 2001 Mazhari CV
## 2001 Noble GP

## 2001 Pandit LV
[Paper](https://doi.org/10.1016/s0006-3495(01)75943-7) Pandit, Clark, Giles, Demir (2001) A Mathematical Model of Action Potential Heterogeneity in Adult Rat Left Ventricular Myocytes

## 2001 Puglisi GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1152/ajpcell.2001.281.6.c2049) Puglisi, Bers (2001) LabHEART; an interactive computer model of rabbit ventricular myocyte ion channels and Ca transport

Known as: Puglisi-Bers, LabHEART

Modifications:
- Rescaled gK1
- ... see Table 1

## 2002 Fenton mV
## 2002 Fox CV
## 2002 Greenstein CV

## 2002 Kneller CA
Base: [Ramirez 2000](#2000-ramirez-ca)
| [Paper](https://doi.org/10.1152/ajpheart.00489.2001) Kneller, Ramirez et al., Nattel (2002) Time-dependent transients in an ionically based mathematical model of the canine atrial action potential

## 2002 Kurata RS
Base: [Wilders 1991](#1991-wilders-ms), [Demir 1994](#1994-demir-rs), [Dokos 1996](#1996-dokos-rs), [Zhang 2000](#2000-zhang-rs)
| [Paper](https://doi.org/10.1152/ajpheart.00900.2001) Kurata, Hisatome, Imanishi, Shibamoto (2002) Dynamical description of sinoatrial node pacemaking; improved mathematical model for primary pacemaker cell

## 2003 Cabo CV
## 2003 Garny

## 2003 Matsuoka mV
[Original code](https://web.archive.org/web/20070819084149/http://www.card.med.kyoto-u.ac.jp/simulation/)
| [Paper](https://doi.org/10.2170/jjphysiol.53.105) Matsuoka, Sarai et al., Noma (2003) Role of individual ionic current systems in ventricular cells hypothesized by a model study

Known as: Kyoto model

Bits:
- Contraction from Negroni 1996
- INaK novel reduced formulation, based on INaCa

## 2003 Mitchell mV

## 2003 Pandit LV
[Paper](https://doi.org/10.1016/s0006-3495(03)74902-9) Pandit, Giles, Demir (2003) A Mathematical Model of the Electrophysiological Alterations in Rat Ventricular Myocytes in Type-I Diabetes

## 2003 Sarai mS
Base: [Matsuoka 2003](#2003-matsuoka-mV)
| [Original code](https://web.archive.org/web/20070819084149/http://www.card.med.kyoto-u.ac.jp/simulation/)
| [Paper](https://doi.org/10.2170/jjphysiol.53.125) Sarai, Matsuoka et al., Noma (2003) Role of individual ionic current systems in the SA node hypothesized by a model study

## 2003 Saucerman LV
## 2003 Seemann HV

## 2004 Bondarenko MV
Base: [Luo 1994](#1994-luo-gv), but many new formulations
| [Paper](https://doi.org/10.1152/ajpheart.00185.2003) Bondarenko, Szigeti et al., Rasmusson (2004) Computer model of action potential of mouse ventricular myocytes

## 2004 Hund CV
Base: [Luo 1994](#1994-luo-gv) (arguably, most of the formulations are new, but the supplement is written in a way that strongly suggests this model was based on Luo 1994).
| [*Updated* code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/01.cir.0000147231.69595.d3) Hund, Rudy (2004) Rate Dependence and Regulation of Action Potential and Calcium Transient in a Canine Cardiac Ventricular Cell Model

Known as: HRd

Bits:
- CaMKII from Hanson et al 1994
- INaCa from Weber et al 2001
- INa from Luo 1994
- INaL from Luo 1994 and Maltsev et al 2001
- Cl regulation from Baumgarten et al [28]
- Iup, Ileak, Itr from Luo 1994
- INaK, IKp, IK1, IpCa from Luo 1994

## 2004 Iyer HV
**Included**
| Base: [Winslow 1999](#1999-winslow-cv) and others
| [Paper](https://doi.org/10.1529/biophysj.104.043299) Iyer, Mazhari, Winslow (2004) A computational model of the human left-ventricular epicardial myocyte

Known as: Iyer-Mazhari-Winslow

## 2004 Lovell RS

## 2004 Shannon RV
Base: [Luo 1994](#1994-luo-gv)? and [Puglisi 2001](#2001-puglisi-gv) ?
| [Likely original matlab code](https://github.com/drgrandilab/Shannon-et-al-2004-Rabbit-Ventricular-Model)
| [Paper](https://doi.org/10.1529/biophysj.104.047449) Shannon, Wang et al., Bers (2004) A mathematical treatment of integrated Ca dynamics within the ventricular myocyte

Known as: Chicago model

Modifications:
- Rescaled gK1
- ...

## 2004 Smith INaK

## 2004 Ten Tusscher HV
**Included**
| [Paper](https://doi.org/10.1152/ajpheart.00794.2003) Ten Tusscher, Noble, Noble, Panfilov (2004) A Model for Human Ventricular Tissue

Known as: TNNP 2004

Bits:
- INa with 3 gates, ref given to Beeler 1977
- ICaL adapted from Luo 1994
- INaK adapted from DiFrancesco 1985

## 2005 Couto LV
## 2005 Flaim CV
## 2005 Krogh-Madsen

## 2005 Kurata HV
[Paper](https://doi.org/10.1529/biophysj.105.060830) Kurata, Hisatome, Matsuda, Shibamoto (2005) Dynamical Mechanisms of Pacemaker Generation in IK1-Downregulated Human Ventricular Myocytes; Insights from Bifurcation Analyses of a Mathematical Model

## 2005 Michailova CV
## 2006 Cortassa mV
## 2006 Fink HV
## 2006 Iribe GV
## 2006 Mangoni MS
## 2006 Pasek LV
## 2006 Sato CV
## 2006 Simitev HA

## 2006a Ten Tusscher HV
**Included**
| Base: [Ten Tusscher 2004](#2004-ten-tusscher-hv)
| [Paper](https://doi.org/10.1152/ajpheart.00109.2006) Ten Tusscher, Panfilov (2006) Alternans and spiral breakup in a human ventricular tissue model

Known as: TP 2006

Modifications:
- Added dyadic subspace
- Changed IKr conductance
- Changed IKs conductance and rates
- Changed ICaL conductance and rates, added gate
- Changed INaK conductance
- Changed IpCa conductance
- New Irel formulation
- Changed Ileak and Iup rate
- Added transfer equations for new subspace

## 2007 Cherry 2007 LA

## 2007 Faber
[Original code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1529/biophysj.106.088807) Faber, Silva, Livshitz, Rudy (2007) Kinetic Properties of the Cardiac L-Type Ca Channel and Its Role in Myocyte Electrophysiology; A Theoretical Investigation

Known as: Faber-Rudy

## 2007 Grandi RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1529/biophysj.107.114868) Grandi, Puglisi et al., Bers (2007) Simulation of Ca-calmodulin-dependent protein kinase II on rabbit ventricular myocyte ion currents and action potentials

## 2007 Livshitz CV
**Included**
| Base: [Hund 2004](#2004-hund-cv)
| [Original code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1152/ajpheart.01347.2006) Livshitz, Rudy (2007) Regulation of Ca and electrical alternans in cardiac myocytes; role of CAMKII and repolarizing currents

## 2007 Niederer LV

## 2007 Terkildsen GV
Bits:
- INaK from Smith 2004, updated by same authors

## 2008 Benson CV
## 2008 Bueno-Orovio HV

## 2008 Fink HV
**Included**
| Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.011) Fink, Noble et al., Giles (2008) Contributions of HERG K current to repolarization of the human ventricular action potential

Modifications:
- New IK1 formulation, based on Yan & Ishihara 2005
- New IKr formulation
- Rescaled IKs

## 2008 Himeno GS
Base: [Sarai 2003](#2003-sarai-ms)
| [Paper](https://doi.org/10.2170/physiolsci.RP015207) Himeno, Sarai, Matsuoka, Noma (2008) Ionic mechanisms underlying the positive chronotropy induced by beta1-adrenergic stimulation in guinea pig sinoatrial node cells

## 2008 Hund CV
Base: [Livshitz 2007](#2007-livshitz-cv)
| [Original code?](https://rudylab.wustl.edu/code-downloads/)

## 2008 Kurata RS

## 2008 Mahajan RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1529/biophysj.106.98160) Mahajan, Shiferaw et al., Weiss (2008) A Rabbit Ventricular Action Potential Model Replicating Cardiac Dynamics at Rapid Heart Rates

## 2008 Pasek GV

## 2008 Ten Tusscher HP
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.026) Ten Tusscher, Panfilov (2008) Modelling of the ventricular conduction system

## 2008 Terkildsen RV
Base: [Pandit 2001](#2001-pandit-lv), Niederer 2006(?), Hinch 2004

## 2008 Saucerman LV
## 2008 Wang LV
## 2009a Aslanidi RA
## 2009b Aslanidi CP

## 2009 Decker CV
**Included**
| Base: [Hund 2008](#2008-hund-cv)
| [Original code](https://rudylab.wustl.edu/code-downloads/)

## 2009 Grandi HV
Base: [Ten Tusscher 2004](#2004-ten-tusscher-hv)

## 2009 Inada mA
Base: [Lindblad 1996](#1996-lindblad-ra), [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1016/j.bpj.2009.06.056) Inada, Hancox, Zhang, Boyett (2009) One-Dimensional Mathematical Model of the Atrioventricular Node Including Atrio-Nodal, Nodal, and Nodal-His Cells

## 2009 Koivumaki MV

## 2009 Livshitz GV
[Original code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/j.bpj.2009.05.062) Livshitz, Rudy (2009) Uniqueness and Stability of Action Potential Models during Rest, Pacing, and Conduction Using Problem-Solving Environment

## 2009 Livshitz CV
[Original code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/j.bpj.2009.05.062) Livshitz, Rudy (2009) Uniqueness and Stability of Action Potential Models during Rest, Pacing, and Conduction Using Problem-Solving Environment

## 2009 Maleckar HA
Base: [Nygren 1998](#1998-nygren-ha)
| [Paper](https://doi.org/10.1152/ajpheart.00411.2009) Maleckar, Greenstein, Giles, Trayanova (2009) K current changes account for the rate dependence of the action potential in the human atrial myocyte

## 2009 Maltsev HS
Base: [Kurata 2002](#2002-kurata-rs), [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1152/ajpheart.01118.2008) Maltsev, Lakatta (2009) Synergism of coupled subsarcolemmal Ca2 clocks and sarcolemmal voltage clocks confers robust and flexible pacemaker function in a novel pacemaker cell model

## 2009 Stewart HP
**Included**
| Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Original CellML](https://models.cellml.org/workspace/stewart_aslanidi_noble_noble_boyett_zhang_2009)
| [Paper](https://doi.org/10.1098/rsta.2008.0283) Stewart, Aslanidi et al., Zhang (2009) Mathematical model of the electrical action potential of Purkinje fibre cells

## 2010 Grandi HV
**Included**
| Base: [Shannon 2004](#2004-shannon-rv)
| [Original matlab code](https://github.com/drgrandilab/Grandi-et-al-2010-Human-Ventricular-Model)
| [Paper](https://doi.org/10.1016/j.yjmcc.2009.09.019) Grandi, Pasqualini, Bers (2010) A novel computational model of the human ventricular action potential and Ca transient

Known as: Grandi-Pasqualini-Bers human ventricular model

Note: Also credited as 2009 due to publication date being listed as 2009 and date of issue it appeared in listed as 2010.

Modifications:
- Scaled gK1
- ...

## 2010 Li MV

## 2010 Sampson HP
**Included**
| Base: [Iyer 2004](#2004-iyer-hv)
| Original code in supplement
| [Paper](https://doi.org/10.1113/jphysiol.2010.187328) Sampson, Iyer, Marks, Kass (2010). A computational model of Purkinje fibre single cell electrophysiology: implications for the long QT syndrome

## 2010 Soltis RV
[Paper](https://doi.org/10.1016/j.bpj.2010.08.016) Soltis, Saucerman (2010) Synergy between CaMKII Substrates and beta-Adrenergic Signaling in Regulation of Cardiac Myocyte Ca2+ Handling

## 2011 Aslanidi HA
## 2011 Carro HV
## 2011 Corrias RP

## 2011 Grandi-Pandit-Voigt HA
**Included**
| Base: [Grandi 2010](#2010-grandi-hv)
| [Original matlab code](https://github.com/drgrandilab/Grandi-et-al-2011-Human-Atrial-Model)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.111.253955) Grandi*, Pandit*, Voigt* et al., Bers (2011) Human atrial action potential and Ca model; sinus rhythm and chronic atrial fibrillation (*shared first authorship)

Modifications:
- Scaled gK1
- ...

## 2011 Heijman CV
**Included**
| Base: [Decker 2009](#2009-decker-cv)
| [Original matlab code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/j.yjmcc.2011.02.007) Heijman, Volders, Westra, Rudy (2011) Local control of beta-adrenergic stimulation; effects on ventricular myocyte electrophysiology and Ca transient

## 2011 Kharche MS
Base: Many
| [Paper](https://doi.org/10.1152/ajpheart.00143.2010) Kharche, Yu, Lei, Zhang (2011) A mathematical model of action potentials of mouse sinoatrial node cells with molecular bases

## 2011 Koivumaki HA
**Included**
| Base: [Nygren 1998](#1998-nygren-ha)
| [Paper](https://doi.org/10.1371/journal.pcbi.1001067) Koivumaki, Korhonen, Tavi (2011) Impact of Sarcoplasmic Reticulum Calcium Release on Calcium Dynamics and Action Potential Morphology in Human Atrial Myocytes; A Computational Study

## 2011 Li CP
Base: [Decker 2009](#2009-decker-cv)
| [Original c++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.111.246512) Li, Rudy (2011) A model of canine purkinje cell electrophysiology and Ca2 cycling; rate dependence, triggered activity, and comparison to ventricular myocytes

Known as: PRd

## 2011 O'Hara HV
**Included**
| Base: [Hund 2004](#2004-hund-cv)
| [Original matlab and C++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1371/journal.pcbi.1002061) O'Hara, Virag, Varro, Rudy (2011) Simulation of the Undiseased Human Cardiac Ventricular Action Potential; Model Formulation and Experimental Validation

Bits:
- INaK from Smith 2004, with reparametrisation

## 2012 Davies

## 2012 Morotti 2012 RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2012-Rabbit-Ventricular-Model-with-Updated-ICaL)
| [Paper](https://doi.org/10.1113/jphysiol.2012.231886) Morotti, Grandi et al., Bers (2012) Theoretical Study of L-type Ca2+ Current Inactivation Kinetics during Action Potential Repolarization and Early Afterdepolarizations

Modifications:
- ICaL model adapted and modified from Mahajan

## 2012 Paci He
Base: [Grandi 2009](#2009-grandi-hv)

## 2012 Severi RS
Base: [Maltsev 2009](#2009-maltsev-hs)
| [Paper](10.1113/jphysiol.2012.229435) Severi, Fantini, Charawi, DiFrancesco (2012) An updated computational model of rabbit sinoatrial action potential to investigate the mechanisms of heart rate modulation

## 2012 Yang HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Modified code](https://github.com/drgrandilab/Fogli-Iseppe-et-al-2021-TdP-prediction)
| [Paper](https://doi.org/10.3389/fphys.2012.00360) Yang, Clancy (2012) In silico Prediction of Sex-Based Differences in Human Susceptibility to Cardiac Ventricular Tachyarrhythmias

## 2013 Colman HA
Base: [Courtemanche 1998](#1998-courtemanche-ha)
| [Paper](https://doi.org/10.1113/jphysiol.2013.254987) Colman, Aslanidi et al., Zhang (2013) Pro-arrhythmogenic effects of atrial fibrillation-induced electrical remodelling: insights from the three-dimensional virtual human atria

## 2013 Paci Hi
**Included**
| Base: [Paci 2012](#2012-paci-he)

## 2013 Voigt-Heijman HA
**Included**
| Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Paper](https://doi.org/10.1016/j.yjmcc.2013.03.011) Voigt, Heijman et al., Dobrev (2013) Impaired Na-dependent regulation of acetylcholine-activated inward-rectifier K current modulates AP rate dependence in cAF

Modifications:
- Added IKAch (Kneller et al. 2002)
- Replaced INa with Courtemanche 1998 one
- Modified IK1 (changed gK1 and a)

## 2014 Chang HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Original OpenCARP code](https://doi.org/10.6084/m9.figshare.1201512)
| [Paper](https://doi.org/10.1371/journal.pcbi.1004011) Chang, Bayer, Trayanova (2014) Disrupted calcium release as a mechanism for atrial alternans associated with human atrial fibrillation

## 2014 Davies MA
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1161/JAHA.113.000340) Davies, Jin et al., Lei (2014) Mkk4 is a negative regulator of the transforming growth factor beta 1 signaling associated with atrial remodeling and arrhythmogenesis with age

## 2014 Morotti MV
Base: [Soltis 2010](#2010-soltis-rv)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2014-Mouse-Ventricular-Model)
| [Paper](https://doi.org/10.1113/jphysiol.2013.266676) Morotti, Edwards et al., Grandi (2014) A novel computational model of mouse myocyte electrophysiology to assess the synergy between Na+ loading and CaMKII

## 2015 Himeno HV
Base: Several! Interesting one to look at

## 2015 Negroni RV
Base: [Shannon 2004](#2004-shannon-rv), [Soltis 2010](#2010-soltis-rv)
| [Original matlab code](https://github.com/drgrandilab/Negroni-et-al-2015-Rabbit-Ventricular-Model-with-Myofilament-Contraction)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.02.014) Negroni, Morotti et al., Bers (2015) Beta-adrenergic effects on cardiac myofilaments and contraction in an integrated rabbit ventricular myocyte model

Bits:
- New myofilament contraction
- Currents, Ca-handling, Na-handling: Shannon 2004
- CaMKII, PKA: Soltis 2010

## 2015 Schmidt

## 2016 Gray RV
**Included**
| Base: New
| [Paper](https://doi.org/10.1371/journal.pcbi.1005087) Gray, Pathmanathan (2016) A Parsimonious Model of the Rabbit Action Potential Elucidates the Minimal Physiological Requirements for Alternans and Spiral Wave Breakup

## 2016 Morotti HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2016-Human-Atrial-Model-with-Updated-INa)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.07.030) Morotti, McCulloch et al., Grandi (2016) Atrial-selective targeting of arrhythmogenic phase-3 earlyafterdepolarizations in human myocytes

Bits:
 - Na modified from Grandi 2007, and (not included): Wagner 2009 & Moreno 2013

## 2016 Passini HV
Base: [O'Hara 2011](#2011-ohara-hv)
[Paper](https://doi.org/10.1016/j.yjmcc.2015.09.003) Passini, Minchole et al. Bueno-Orovio (2016 ) Mechanisms of Pro-Arrhythmic Abnormalities in Ventricular Repolarisation and Anti-Arrhythmic Therapies in Human Hypertrophic Cardiomyopathy

Modifications:
- Rescaled Ito
- Changed concentrations
- Constant EK
- Shifted act/inact curves INa, INaL, IK1
- Modified INa steady states

## 2016 Varela CA

## 2017 Bartos RV
Base: [Negroni 2015](#2015-negroni-rv)
| [Original matlab code](https://github.com/drgrandilab/Bartos-et-al-2017-Rabbit-Ventricular-Model-with-Updated-IKs)
| [Paper](https://doi.org/10.1113/JP273676) Bartos, Morotti et al., Bers (2017) Quantitative analysis of the Ca2+-dependent regulation of delayed rectifier K+ current IKs in rabbit ventricular myocytes

Bits:
- New IKs with Ca regulation

## 2017 Colman HA
Base: [Colman 2013](#2013-colman-ha)
| [Paper](https://doi.org/10.1371/journal.pcbi.1005587) Colman, Ni et al., Zhang (2017) In silico assessment of genetic variation in KCNA5 reveals multiple mechanisms of human atrial arrhythmogenesis

## 2017 Dutta HV
**Included**
| Base: [Li 2017](#2017-li-hv)
| [Official CellML](https://models.cellml.org/e/4e8/ohara_rudy_cipa_v1_2017.cellml/view)

Known as: ORd-cipa-v1

Modifications:
- Rescaling of conductances to better predict drug effects

## 2017 Ellinwood HA
Base: [Morotti 2016](#2016-morotti-ha)
| [Original matlab code](https://github.com/drgrandilab/Ellinwood-et-al-2017-Human-Atrial-Model-with-Updated-IKur)
| [Paper](https://doi.org/10.1063/1.5000226) Ellinwood, Dobrev, Morotti, Grandi (2017) Revealing kinetics and state-dependent binding properties of IKur-targeting drugs that maximize atrial fibrillation selectivity [Erratum](https://doi.org/10.1063/1.5007051)

Bits:
- IKur adapted from 
Zhou et al. (PLoS ONE 2012; e42295)

## 2017 Fabbri HS
Base: [Severi 2012](#2012-severi-rs)
| [Official CellML](https://www.mcbeng.it/en/downloads/software/hap-san.html)
| [Physiome reproduction](https://doi.org/10.36903/physiome.16550526)
| [Paper](https://doi.org/10.1113/JP273259) Fabbri, Fantini, Wilders, Severi (2017) Computational analysis of the human sinus node action potential; model development and effects of mutations

## 2017 Li 2017 HV
**Included**
| Base: [O'Hara 2011](#2011-ohara-hv)

Known as: IKr-dynamic ORd model, original IKr-dyn ORd model

Modifications:
- New IKr model with drug trapping

## 2017 Ni HA
**Included**
| Base: [Colman 2017](#2017-colman-ha)
| [Paper](https://doi.org/10.3389/fphys.2017.00946) Ni, Whittaker et al., Zhang (2017) Synergistic Anti-arrhythmic Effects in Human Atria with Combined Use of Sodium Blockers and Acacetin

Bits:
- Calcium subspaces based on Koivumaki 2011

## 2017 Surdo MV
Base: [Morotti 2014](#2014-morotti-mv) 
| [Original matlab code](https://github.com/drgrandilab/Surdo-et-al-2017-Mouse-Ventricular-Model-with-Myofilament-Contraction)
| [Paper](https://doi.org/10.1038/ncomms15031) Surdo, Berrera et al., Zaccolo (2017) FRET biosensor uncovers cAMP nano-domains at beta-adrenergic targets that dictate precise tuning of cardiac contractility

Bits:
- Myofilament contraction from Negroni 2015

## 2018 Bai HA
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Official CellML](https://models.cellml.org/workspace/520)
| [Paper](https://doi.org/10.1038/s41598-018-33958-y) Bai, Gladding et al., Zhao (2018) Ionic and cellular mechanisms underlying TBX5-PITX2 insufficiency-induced atrial fibrillation; Insights from mathematical models of human atrial cells

## 2018 Colman HA
Base: This model has 4 variants
| [Original code](https://github.com/michaelcolman/hAM_WL)
| [Paper](https://doi.org/10.3389/fphys.2018.01211) Colman, Saxena, Kettlewell, Workman (2018) Description of the Human Atrial Action Potential Derived From a Single, Congruent Data Source; Novel Computational Models for Integrated Experimental-Numerical Study of Atrial Arrhythmia Mechanisms

## 2018 Paci Hi
**Included**
| Base: [Paci 2013](#2013-paci-hi)
| [Paper](https://doi.org/10.3389/fphys.2018.00709) Paci, Polonen et al., Hyttinen (2018) Automatic optimization of an in silico model of human iPSC derived cardiomyocytes recapitulating calcium handling abnormalities

## 2018 Sutanto HA

## Loewe 2019 HS
Base: [Fabbri 2017](#2017-fabbri-hs)
| [Official CellML](https://models.physiomeproject.org/workspace/58f)
| [Paper](https://doi.org/10.1016/j.bpj.2019.07.037) Loewe, Lutz et al., Severi (2019) Hypocalcemia-Induced Slowing of Human Sinus Node Pacemaking

## 2019 Kernik Hi
**Included**
| Base: [Shannon 2004](#2004-shannon-rv), [Ten Tusscher 2004](#2004-ten-tusscher-hv), [Maltsev 2009](#2009-maltsev-hs)
| [Paper](https://doi.org/10.1113/jp277724) Kernik, Morotti et al., Clancy (2019) A computational model of induced pluripotent stem‐cell derived cardiomyocytes incorporating experimental variability from multiple data sources

## 2019 Tomek HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Original Matlab and official CellML](https://github.com/jtmff/torord/commit/4ffab13b48f0923d38b0315f26be466a6fad8b70)
| [Paper](https://doi.org/10.7554/elife.48890) Tomek, Bueno-Orovio et al., Rodriguez (2019) Development, calibration, and validation of a novel human ventricular myocyte model in health, disease, and drug block

## 2020 Bartolucci HV
Base: [Dutta 2017](#2017-dutta-hv)
| [Original matlab code](https://www.mcbeng.it/en/downloads/software/16-bps2020-model.html)
| [Official CellML](https://models.physiomeproject.org/workspace/5fd)
| [Paper](https://doi.org/10.3389/fphys.2020.00314) Bartolucci, Passini et al., Severi (2020) Simulation of the effects of extracellular calcium changes leads to a novel computational model of human ventricular action potential with a revised calcium handling

Known as: BPS2020

Modifications:
- New ICaL formulation
- ...

## 2020 Paci Hi
**Included**
| Base: [Paci 2018](#2018-paci-hi)
| [Paper](https://doi.org/10.1016/j.bpj.2020.03.018) Paci, Passini et al., Entcheva (2020) All-Optical Electrophysiology Refines Populations of In Silico Human iPSC-CMs for Drug Evaluation

## 2020 Tomek HV
Base: [Tomek 2019](#2019-tomek-hv)
| [Original Matlab and official CellML](https://github.com/jtmff/torord)
| [Paper](https://doi.org/10.1101/2020.06.01.127043) Tomek, Bueno-Orovio, Rodriguez (2020) ToR-ORd-dynCl; an update of the ToR-ORd model of human ventricular cardiomyocyte with dynamic intracellular chloride

## 2020 Trovato HP
**Included**
| Base: [O'Hara 2011](#2011-ohara-hv), [Li 2011](#2011-li-cp)
| [Original Matlab and official CellML](https://www.cs.ox.ac.uk/insilicocardiotox/purkinje-models)
| [Paper](https://doi.org/10.1016/j.yjmcc.2020.04.001) Trovato, Passini et al., Rodriguez (2020) Human Purkinje in silico model enables mechanistic investigations into automaticity and pro-arrhythmic abnormalities

Modifications:
- INa from Passini 2016
- ...

## 2021 Akwaboah Hi
**Included**
| Base: [Kurata 2002](#2002-kurata-rs) and [Courtemanche 1998](#1998-courtemanche-ha)

Bits:
- INa from Luo 1991, with partial reparameterisation
- Ito from Grandi 2010, with partial reparametrisation
- IKr from Kurata 2002, with partial reparametrisation
- If from Stewart 2009, with partial reperametrisation
- ICaL from Kurata 2002, with partial reparametrisation
- IKs from Courtemanche 1998
- IKur from Courtemanche 1998
- INaK from Courtemanche 1998
- INaCa from Courtemanche 1998
- IKACh from Kurata 2002
- IK1 from Grandi 2010
- IbCa from Courtemanche 1998
- IbNa from Courtemanche 1998
- IpCa from Courtemanche 1998
- Calcium handling from Kurata 2002

## 2021 Fogli Iseppe HV
Base: [Yang 2012](#2012-yang-hv)
| [Original C++ code](https://github.com/drgrandilab/Fogli-Iseppe-et-al-2021-TdP-prediction)
| [Paper](https://doi.org/10.1002/cpt.2240) Fogli Iseppe, Ni et al., Grandi (2021) Sex-specific classification of drug-induced Torsade de Pointes susceptibility using cardiac simulations and machine learning

## 2021 Gaur PV
[Paper](https://doi.org/10.1371/journal.pcbi.1009137) Gaur, Qi et al., Vigmond (2021) A computational model of pig ventricular cardiomyocyte electrophysiology and calcium handling; Translation from pig to human electrophysiology

## 2021 Morotti MS
Base: [Kharche 2011](#2011-kharche-ms)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2021-mouse-sinoatrial-model)
| [Paper](https://doi.org/10.3390/ijms22115645) Morotti, Ni et al., Grandi (2021) Intracellular Na+ Modulates Pacemaking Activity in Murine Sinoatrial Node Myocytes: An In Silico Analysis

## 2022 Bartolucci HV
Base: [Bartoluci 2020](#2020-bartolucci-hv)
| [Paper](https://doi.org/10.3389/fphys.2022.906146) Bartolucci, Forouzandemehr, Severi, Paci (2022) A Novel In Silico Electromechanical Model of Human Ventricular Cardiomyocyte

Known as: BPSLand

Modifications:
- Added Land 2017 contraction model
- ...

## 2022 Kohjitani Hi
Base: [Himeno 2015](#2015-himeno-hv)
| [Paper](https://doi.org/10.1038/s41598-022-23398-0) Kohjitani, Koda et al., Kimura (2022) Gradient-based parameter optimization method to determine membrane ionic current composition in human induced pluripotent stem cell-derived cardiomyocytes

## 2022 Mahzar HA
Base: [Koivumaki 2011](#2011-koivumaki-ha), Regazzoni 2020
| [Paper](https://doi.org/10.1113/JP283974) Mazhar, Bartolucci et al., Severi (2023) A detailed mathematical model of the human atrial cardiomyocyte: integration of electrophysiology and cardiomechanics

Known as: MBS2023





## 2022 Moise
[Paper](https://doi.org/10.1016/j.bpj.2023.03.024) Moise, Weinberg (2022) Emergent Electrical Activity, Tissue Heterogeneity, and Robustness in a Calcium Feedback Regulatory Model of the Sinoatrial Node


## 2023 Heijman HA
Base: Grandi 2011? Or voigt-heijman?
| [Original matlab code](https://github.com/drgrandilab/Heijman-et-al-2023-Human-Atrial-Model)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.122.321858) Heijman, Zhou et al., Dobrev (2023) Enhanced Ca-Dependent SK-Channel Gating and Membrane Trafficking in Human Atrial Fibrillation

## 2023 Herrera HA
Base: [Ellinwood 2017](#2017-ellinwood-ha)
| [Original matlab code](https://github.com/drgrandilab/Herrera-et-al-2023-Human-Atrial-Model)
| [Paper](https://doi.org/10.1152/ajpheart.00362.2023) Herrera, Zhang et al., Morotti (2023) Dual effects of the small-conductance Ca-activated K current on human atrial electrophysiology and Ca-driven arrhythmogenesis; an in silico study

Also cites a 2020 Ni paper, but that refers to Ellinwood.

## 2023 Ni HA
Base: [Morotti 2017](#2016-morotti-ha)
| [Original C++ code](https://github.com/drgrandilab/Ni-et-al-2023-Human-Atrial-Signaling-Model)
| [Paper](https://doi.org/10.1093/cvr/cvad118) Ni, Morotti et al., Grandi (2023) Integrative human atrial modelling unravels interactive PKA and CaMKII signalling as key determinants of atrial arrhythmogenesis









.
