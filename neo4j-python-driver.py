from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "neo4j://44.202.204.14:7687",
  auth=basic_auth("neo4j", "rifling-ambiguity-elbow"))

cypher_query = '''
MATCH (a:Airport{iata:$iata})-[r:HAS_ROUTE]->(other)
  RETURN other.iata as destination
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      iata="DEN").data())
  for record in results:
    print(record['destination'])

driver.close()

print("all done")
