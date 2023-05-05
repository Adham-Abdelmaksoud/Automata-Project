# Automata Project

## Dependencies

to install all Python dependencies run the following command in the root directory of the project

```ssh
pip install -r requirements.txt

```

for graphviz please visit [graphviz.org](https://graphviz.org/download/) to download the installer and follow the default settings to install it and tick the option to add it to the path.

## NFA to DFA conversion

### User instructions

#### To Create your NFA:

1. Choose the starting node and mark the node as initial if it is the initial node.
2. Choose the destination node and mark it as final if it is a final node.
3. Enter the transition edge value.
4. Press Add Edge.
5. Repeat (1-4) until finish.

#### To Generate Random NFA Graph:

Press Generate Random NFA.

#### To Convert NFA to DFA:

Press Convert NFA to DFA.

Press Clear Graph to start again

#### Note that:

1. There must be one and only one Initial Node.
2. There must be at least one Final Node
3. To enter an empty string (Ɛ): Type (eps)
4. Each time you enter a node you must enter all its details (whether its initial final)

## CFG to PDA conversion

### User instructions
