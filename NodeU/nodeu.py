from OP_RETURN import *


def write_on_chain(data,testnet=False):#data must smaller than 220 bytes
	data_from_hex=OP_RETURN_hex_to_bin(data)
	if data_from_hex is not None:
		data=data_from_hex

	result=OP_RETURN_store(data, testnet)

	if 'error' in result:
		print('Error: '+result['error'])
	else:
		print("TxIDs:\n"+"\n".join(result['txids'])+"\n\nRef: "+result['ref'])
	return result['txids'][0]

#print(write_on_chain("Info write on blockchain.",True))
