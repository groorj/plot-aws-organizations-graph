# https://graphviz.readthedocs.io/en/stable/examples.html
import json
import graphviz

g = graphviz.Digraph('organizations', filename='my-org.gv', format='pdf',
                     node_attr={'color': 'lightblue2', 'style': 'filled'})

g.attr(rankdir='TB', size='10')

f = open('output.json')
data = json.load(f)
for i in data['Accounts']:
    number_of_nodes = len(data['Accounts'])
    print(i)
    text=i['Name'] + '\n\n' + i['Id']
    g.node('Root')
    g.node(i['Name'])
    g.edge('Root', i['Name'])
f.close()
stagger_number=round(number_of_nodes/5)
print(stagger_number)
u = g.unflatten(stagger=stagger_number)
u.view()

#g.view()

# End;
