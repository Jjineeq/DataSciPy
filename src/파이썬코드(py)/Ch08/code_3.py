partyA = set(['Park','Kim','Lee'])
partyB = set(['Park','Choi'])

print("Party A and PartyB attend people", partyA.union(partyB))
print("Party A, PartyB attend people", partyA.symmetric_difference(partyB))
print("Party A attend people", partyA.difference(partyB))