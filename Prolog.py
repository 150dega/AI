% Facts (Basic Relationships)

parent(john, mary).
parent(john, david).
parent(susan, mary).
parent(susan, david).
parent(mary, alice).

male(john).
male(david).

female(susan).
female(mary).
female(alice).

% Rules

father(X, Y) :- parent(X, Y), male(X).

mother(X, Y) :- parent(X, Y), female(X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

grandfather(X, Y) :- grandparent(X, Y), male(X).

grandmother(X, Y) :- grandparent(X, Y), female(X).

'''% Sample Queries

?- father(john, mary).
?- mother(susan, david).
?- sibling(mary, david).
?- grandparent(john, alice).'''
