SOURCE="https://www.theguardian.com/politics/2022/jun/08/tory-rebels-wait-for-boris-johnson-to-blow-himself-up-to-trigger-fresh-vote"
ENTITIES="ORG PERSON DATE"

python3 main.py -s $SOURCE -e $ENTITIES

expected_output='
    ---------- RESULTS ----------
    Entity: "ORG"
    Found:  7
    Results: the 1922 Committee, LBC, Guardian, Johnson’s Downing Street, the Foreign Office, Rubicon, Partygate
    

    ---------- RESULTS ----------
    Entity: "PERSON"
    Found:  16
    Results: Nusrat Ghani, William Wragg, Geoffrey Clifton-Brown, Jeremy Hunt, Nadhim Zahawi, Johnson, Tiverton, Lady Morrissey, Penny Mordaunt, Morrissey, Liz Truss, Helena Morrissey, Owen Paterson, Boris Johnson, Tom Tugendhat, Graham Brady
    

    ---------- RESULTS ----------
    Entity: "DATE"
    Found:  12
    Results: the coming weeks, six months, the summer, 23 June, Wednesday, Monday, September 2020, 12-month, this week, 12 months, last weekend, next June
'