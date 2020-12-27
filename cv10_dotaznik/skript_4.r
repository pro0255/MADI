# skript je napsan "hrubou silou" :-) tak aby bylo jednoduche pochopit jednotlive prikazy 
library(igraph)
library(ggplot2)
library(tidyverse)

f <- "studenti predmety.csv"
#f <- "actors and movies.csv"
# nacteni dat do dataframu
df <- read.csv2(f, header =TRUE, stringsAsFactors=F)
dim(df)

# prevod na objekt "typu" igraph
g <- graph.data.frame(df, directed = FALSE) 
V(g)$type <- V(g)$name %in% df[,1]
g

# matice sousednosti bipartitniho grafu
bipartite_matrix <- as_incidence_matrix(g)
##############################

# one-mode projekce
A <- t(bipartite_matrix) %*% bipartite_matrix 
diag(A) <- 0
A

B <-  bipartite_matrix %*% t(bipartite_matrix) 
## crossprod() does same and scales better
diag(B) <- 0
B

gA <- graph_from_adjacency_matrix(A,mode = "undirected", weighted = TRUE)
gA

gB <- graph_from_adjacency_matrix(B,mode = "undirected", weighted = TRUE)
gB

# vypocet vah hran
E(gA)$weight
E(gB)$weight

# prevod na dataframe
Adf <- get.data.frame(gA)
Bdf <- get.data.frame(gB)

write.table(Adf, file="studenti.csv", sep=";", row.names = FALSE, col.names=FALSE)
write.table(Bdf, file="predmety.csv", sep=";", row.names = FALSE, col.names=FALSE)

#write.table(Adf, file="actors.csv", sep=";", row.names = FALSE, col.names=FALSE)
#write.table(Bdf, file="movies.csv", sep=";", row.names = FALSE, col.names=FALSE)

#######################
# export do formatu pro Gephi
# zkusme ulozit jako gml, ve vyslednem gml souboru ulozi jmenovkx jako "name", lepsi by bylo "label"
# pak muze byt problem v Gephi v nahledu se jmenovkama

write.graph(graph = gA, file = "gA.gml", format = "gml")
write.graph(graph = gB, file = "gB.gml", format = "gml")

#######################
# export do formatu pro Gephi
# zkusme ulozit jako gexf - lepsi volba

library(rgexf)

g1.gexf <- igraph.to.gexf(gA)
# 
f <- file("gA.gexf")
writeLines(g1.gexf$graph, con = f)
close(f)

g2.gexf <- igraph.to.gexf(gB)
# 
f <- file("gB.gexf")
writeLines(g2.gexf$graph, con = f)
close(f)

# rm(list = ls())

