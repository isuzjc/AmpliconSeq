from opentrons import protocol_api
import csv

# metadata
metadata = {
	'protocolName': 'Make Index Plates', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Make 5uM index plates',
	'apiLevel': '2.7'
}

ForwardLoading = '''
SourceWell,i5,TargetWells
Indexes_A1,i5_F1_515rcbc110,Plate1_A1;Plate1_B1;Plate1_C1;Plate1_D1;Plate1_E1;Plate1_F1;Plate1_G1;Plate1_H1;Plate2_A1;Plate2_B1;Plate2_C1;Plate2_D1;Plate2_E1;Plate2_F1;Plate2_G1;Plate2_H1;Plate3_A1;Plate3_B1;Plate3_C1;Plate3_D1;Plate3_E1;Plate3_F1;Plate3_G1;Plate3_H1
Indexes_B1,i5_F2_515rcbc184,Plate1_A2;Plate1_B2;Plate1_C2;Plate1_D2;Plate1_E2;Plate1_F2;Plate1_G2;Plate1_H2;Plate2_A2;Plate2_B2;Plate2_C2;Plate2_D2;Plate2_E2;Plate2_F2;Plate2_G2;Plate2_H2;Plate3_A2;Plate3_B2;Plate3_C2;Plate3_D2;Plate3_E2;Plate3_F2;Plate3_G2;Plate3_H2
Indexes_C1,i5_F3_515rcbc434,Plate1_A3;Plate1_B3;Plate1_C3;Plate1_D3;Plate1_E3;Plate1_F3;Plate1_G3;Plate1_H3;Plate2_A3;Plate2_B3;Plate2_C3;Plate2_D3;Plate2_E3;Plate2_F3;Plate2_G3;Plate2_H3;Plate3_A3;Plate3_B3;Plate3_C3;Plate3_D3;Plate3_E3;Plate3_F3;Plate3_G3;Plate3_H3
Indexes_D1,i5_F4_515rcbc443,Plate1_A4;Plate1_B4;Plate1_C4;Plate1_D4;Plate1_E4;Plate1_F4;Plate1_G4;Plate1_H4;Plate2_A4;Plate2_B4;Plate2_C4;Plate2_D4;Plate2_E4;Plate2_F4;Plate2_G4;Plate2_H4;Plate3_A4;Plate3_B4;Plate3_C4;Plate3_D4;Plate3_E4;Plate3_F4;Plate3_G4;Plate3_H4
Indexes_E1,i5_F5_515rcbc551,Plate1_A5;Plate1_B5;Plate1_C5;Plate1_D5;Plate1_E5;Plate1_F5;Plate1_G5;Plate1_H5;Plate2_A5;Plate2_B5;Plate2_C5;Plate2_D5;Plate2_E5;Plate2_F5;Plate2_G5;Plate2_H5;Plate3_A5;Plate3_B5;Plate3_C5;Plate3_D5;Plate3_E5;Plate3_F5;Plate3_G5;Plate3_H5
Indexes_F1,i5_F6_515rcbc587,Plate1_A6;Plate1_B6;Plate1_C6;Plate1_D6;Plate1_E6;Plate1_F6;Plate1_G6;Plate1_H6;Plate2_A6;Plate2_B6;Plate2_C6;Plate2_D6;Plate2_E6;Plate2_F6;Plate2_G6;Plate2_H6;Plate3_A6;Plate3_B6;Plate3_C6;Plate3_D6;Plate3_E6;Plate3_F6;Plate3_G6;Plate3_H6
Indexes_G1,i5_F7_515rcbc621,Plate1_A7;Plate1_B7;Plate1_C7;Plate1_D7;Plate1_E7;Plate1_F7;Plate1_G7;Plate1_H7;Plate2_A7;Plate2_B7;Plate2_C7;Plate2_D7;Plate2_E7;Plate2_F7;Plate2_G7;Plate2_H7;Plate3_A7;Plate3_B7;Plate3_C7;Plate3_D7;Plate3_E7;Plate3_F7;Plate3_G7;Plate3_H7
Indexes_H1,i5_F8_515rcbc628,Plate1_A8;Plate1_B8;Plate1_C8;Plate1_D8;Plate1_E8;Plate1_F8;Plate1_G8;Plate1_H8;Plate2_A8;Plate2_B8;Plate2_C8;Plate2_D8;Plate2_E8;Plate2_F8;Plate2_G8;Plate2_H8;Plate3_A8;Plate3_B8;Plate3_C8;Plate3_D8;Plate3_E8;Plate3_F8;Plate3_G8;Plate3_H8
Indexes_A2,i5_F9_515rcbc679,Plate1_A9;Plate1_B9;Plate1_C9;Plate1_D9;Plate1_E9;Plate1_F9;Plate1_G9;Plate1_H9;Plate2_A9;Plate2_B9;Plate2_C9;Plate2_D9;Plate2_E9;Plate2_F9;Plate2_G9;Plate2_H9;Plate3_A9;Plate3_B9;Plate3_C9;Plate3_D9;Plate3_E9;Plate3_F9;Plate3_G9;Plate3_H9
Indexes_B2,i5_F10_515rcbc695,Plate1_A10;Plate1_B10;Plate1_C10;Plate1_D10;Plate1_E10;Plate1_F10;Plate1_G10;Plate1_H10;Plate2_A10;Plate2_B10;Plate2_C10;Plate2_D10;Plate2_E10;Plate2_F10;Plate2_G10;Plate2_H10;Plate3_A10;Plate3_B10;Plate3_C10;Plate3_D10;Plate3_E10;Plate3_F10;Plate3_G10;Plate3_H10
Indexes_C2,i5_F11_515rcbc789,Plate1_A11;Plate1_B11;Plate1_C11;Plate1_D11;Plate1_E11;Plate1_F11;Plate1_G11;Plate1_H11;Plate2_A11;Plate2_B11;Plate2_C11;Plate2_D11;Plate2_E11;Plate2_F11;Plate2_G11;Plate2_H11;Plate3_A11;Plate3_B11;Plate3_C11;Plate3_D11;Plate3_E11;Plate3_F11;Plate3_G11;Plate3_H11
Indexes_D2,i5_F12_515rcbc950,Plate1_A12;Plate1_B12;Plate1_C12;Plate1_D12;Plate1_E12;Plate1_F12;Plate1_G12;Plate1_H12;Plate2_A12;Plate2_B12;Plate2_C12;Plate2_D12;Plate2_E12;Plate2_F12;Plate2_G12;Plate2_H12;Plate3_A12;Plate3_B12;Plate3_C12;Plate3_D12;Plate3_E12;Plate3_F12;Plate3_G12;Plate3_H12
Indexes_E2,i5_F13_515rcbc258,Plate4_A1;Plate4_B1;Plate4_C1;Plate4_D1;Plate4_E1;Plate4_F1;Plate4_G1;Plate4_H1;Plate5_A1;Plate5_B1;Plate5_C1;Plate5_D1;Plate5_E1;Plate5_F1;Plate5_G1;Plate5_H1;Plate6_A1;Plate6_B1;Plate6_C1;Plate6_D1;Plate6_E1;Plate6_F1;Plate6_G1;Plate6_H1
Indexes_F2,i5_F14_515rcbc277,Plate4_A2;Plate4_B2;Plate4_C2;Plate4_D2;Plate4_E2;Plate4_F2;Plate4_G2;Plate4_H2;Plate5_A2;Plate5_B2;Plate5_C2;Plate5_D2;Plate5_E2;Plate5_F2;Plate5_G2;Plate5_H2;Plate6_A2;Plate6_B2;Plate6_C2;Plate6_D2;Plate6_E2;Plate6_F2;Plate6_G2;Plate6_H2
Indexes_G2,i5_F15_515rcbc472,Plate4_A3;Plate4_B3;Plate4_C3;Plate4_D3;Plate4_E3;Plate4_F3;Plate4_G3;Plate4_H3;Plate5_A3;Plate5_B3;Plate5_C3;Plate5_D3;Plate5_E3;Plate5_F3;Plate5_G3;Plate5_H3;Plate6_A3;Plate6_B3;Plate6_C3;Plate6_D3;Plate6_E3;Plate6_F3;Plate6_G3;Plate6_H3
Indexes_H2,i5_F16_515rcbc707,Plate4_A4;Plate4_B4;Plate4_C4;Plate4_D4;Plate4_E4;Plate4_F4;Plate4_G4;Plate4_H4;Plate5_A4;Plate5_B4;Plate5_C4;Plate5_D4;Plate5_E4;Plate5_F4;Plate5_G4;Plate5_H4;Plate6_A4;Plate6_B4;Plate6_C4;Plate6_D4;Plate6_E4;Plate6_F4;Plate6_G4;Plate6_H4
Indexes_A3,i5_F17_515rcbc762,Plate4_A5;Plate4_B5;Plate4_C5;Plate4_D5;Plate4_E5;Plate4_F5;Plate4_G5;Plate4_H5;Plate5_A5;Plate5_B5;Plate5_C5;Plate5_D5;Plate5_E5;Plate5_F5;Plate5_G5;Plate5_H5;Plate6_A5;Plate6_B5;Plate6_C5;Plate6_D5;Plate6_E5;Plate6_F5;Plate6_G5;Plate6_H5
Indexes_B3,i5_F18_515rcbc797,Plate4_A6;Plate4_B6;Plate4_C6;Plate4_D6;Plate4_E6;Plate4_F6;Plate4_G6;Plate4_H6;Plate5_A6;Plate5_B6;Plate5_C6;Plate5_D6;Plate5_E6;Plate5_F6;Plate5_G6;Plate5_H6;Plate6_A6;Plate6_B6;Plate6_C6;Plate6_D6;Plate6_E6;Plate6_F6;Plate6_G6;Plate6_H6
Indexes_C3,i5_F19_515rcbc800,Plate4_A7;Plate4_B7;Plate4_C7;Plate4_D7;Plate4_E7;Plate4_F7;Plate4_G7;Plate4_H7;Plate5_A7;Plate5_B7;Plate5_C7;Plate5_D7;Plate5_E7;Plate5_F7;Plate5_G7;Plate5_H7;Plate6_A7;Plate6_B7;Plate6_C7;Plate6_D7;Plate6_E7;Plate6_F7;Plate6_G7;Plate6_H7
Indexes_D3,i5_F20_515rcbc844,Plate4_A8;Plate4_B8;Plate4_C8;Plate4_D8;Plate4_E8;Plate4_F8;Plate4_G8;Plate4_H8;Plate5_A8;Plate5_B8;Plate5_C8;Plate5_D8;Plate5_E8;Plate5_F8;Plate5_G8;Plate5_H8;Plate6_A8;Plate6_B8;Plate6_C8;Plate6_D8;Plate6_E8;Plate6_F8;Plate6_G8;Plate6_H8
Indexes_E3,i5_F21_515rcbc858,Plate4_A9;Plate4_B9;Plate4_C9;Plate4_D9;Plate4_E9;Plate4_F9;Plate4_G9;Plate4_H9;Plate5_A9;Plate5_B9;Plate5_C9;Plate5_D9;Plate5_E9;Plate5_F9;Plate5_G9;Plate5_H9;Plate6_A9;Plate6_B9;Plate6_C9;Plate6_D9;Plate6_E9;Plate6_F9;Plate6_G9;Plate6_H9
Indexes_F3,i5_F22_515rcbc867,Plate4_A10;Plate4_B10;Plate4_C10;Plate4_D10;Plate4_E10;Plate4_F10;Plate4_G10;Plate4_H10;Plate5_A10;Plate5_B10;Plate5_C10;Plate5_D10;Plate5_E10;Plate5_F10;Plate5_G10;Plate5_H10;Plate6_A10;Plate6_B10;Plate6_C10;Plate6_D10;Plate6_E10;Plate6_F10;Plate6_G10;Plate6_H10
Indexes_G3,i5_F23_515rcbc885,Plate4_A11;Plate4_B11;Plate4_C11;Plate4_D11;Plate4_E11;Plate4_F11;Plate4_G11;Plate4_H11;Plate5_A11;Plate5_B11;Plate5_C11;Plate5_D11;Plate5_E11;Plate5_F11;Plate5_G11;Plate5_H11;Plate6_A11;Plate6_B11;Plate6_C11;Plate6_D11;Plate6_E11;Plate6_F11;Plate6_G11;Plate6_H11
Indexes_H3,i5_F24_515rcbc925,Plate4_A12;Plate4_B12;Plate4_C12;Plate4_D12;Plate4_E12;Plate4_F12;Plate4_G12;Plate4_H12;Plate5_A12;Plate5_B12;Plate5_C12;Plate5_D12;Plate5_E12;Plate5_F12;Plate5_G12;Plate5_H12;Plate6_A12;Plate6_B12;Plate6_C12;Plate6_D12;Plate6_E12;Plate6_F12;Plate6_G12;Plate6_H12
'''

ReverseLoading = '''
SourceWell,TargetPlate
A4,Plate1
A4,Plate4
A5,Plate2
A5,Plate5
A6,Plate3
A6,Plate6
'''

# Use the lines below to bypass steps (False to bypass)
loadforward = True
loadreverse = True
volume = 40 #add 40ul of each index for 80 per well combined
space = 2 # multichannel reverse indexes from 2mm above well

def run(protocol: protocol_api.ProtocolContext):

	# define labware and locations
	Plate1= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1') # skirted 96 well plate containing arrayed indexes
	Plate2= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2') # skirted 96 well plate containing arrayed indexes
	Plate3= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '3') # skirted 96 well plate containing arrayed indexes
	Plate4= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '4') # skirted 96 well plate containing arrayed indexes
	Plate5= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5') # skirted 96 well plate containing arrayed indexes
	Plate6= protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6') # skirted 96 well plate containing arrayed indexes

	Indexes= protocol.load_labware('vwr_96_wellplate_2000ul', '7') # VWR deep well plate (75870-796) containing 1mL of each index at 10uM

	tips200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '8') # 20ul filter tips on deck position 1
	tips1000 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', '9') # 20ul filter tips on deck position 1

	# define pipettes
	left_pipette = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips1000])
	right_pipette = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tips200])
		
	###############################		
	#load the forward indexes one at a time	using single channel
	if loadforward:
		loadings_parsed = ForwardLoading.splitlines()[1:] # Discard the blank first line.
		for load in csv.DictReader(loadings_parsed):
			left_pipette.pick_up_tip()
			
			source=load['SourceWell']
			source=source.split("_")
			source_plate=source[0]
			source_well=source[1]
			
			target=load['TargetWells']
			target=target.split(";")
			
			left_pipette.aspirate(24.5*volume, eval(source_plate)[source_well]) 

			for targ in target:
				targ=targ.split("_")
				target_plate=targ[0]
				target_well=targ[1]
				left_pipette.dispense(volume, eval(target_plate)[target_well])

			left_pipette.drop_tip()	 
	
	###############################	
	#load the reverse indexes using multichannel
	if loadreverse:
		loadings_parsed = ReverseLoading.splitlines()[1:] # Discard the blank first line.
		for load in csv.DictReader(loadings_parsed):
			right_pipette.pick_up_tip()
			for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
				right_pipette.aspirate(volume, Indexes[load['SourceWell']])
				right_pipette.dispense(volume, eval(load['TargetPlate'])['A'+str(i)].top(space))
				right_pipette.aspirate(volume, eval(load['TargetPlate'])['A'+str(i)].top(space))			
				right_pipette.dispense(volume, Indexes[load['SourceWell']].top(-4))
			right_pipette.touch_tip()
			right_pipette.drop_tip()
	
	
	
