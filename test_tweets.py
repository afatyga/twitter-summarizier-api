import twitterHW2

def test_compare():
#	assert twitterHW2.getMsgs("alexfatyga_") == twitterHW2.getMsgs("alexfatyga_") 
	assert twitterHW2.getMsgs(0) == "0"
	assert twitterHW2.getMsgs("fakefakefakeusername1234211") == "0"
