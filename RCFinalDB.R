## Package installation
install.packages("dplyr")
install.packages('stringi')

#Libraries
library(dplyr)
library(stringi)


#setwd()

dfAll = read.csv('data/enamoratec.csv')


#Leer datos, se agrega 1 por indice 0
dfCasual = read.csv('results/casual-valentines', header = FALSE)
dfCasual$V1 = (as.numeric(dfCasual$V1))+1
dfCasual$V2 = (as.integer(dfCasual$V2))+1
dfCasual$V4 = (as.numeric(dfCasual$V4))+1
dfCasual$V6 = (as.numeric(dfCasual$V6))+1
dfRelation = read.csv('results/relationship-valentines', header = FALSE)
dfRelation$V1 = (as.numeric(dfRelation$V1))+1
dfRelation$V2 = (as.numeric(dfRelation$V2))+1
dfRelation$V4 = (as.numeric(dfRelation$V4))+1
dfRelation$V6 = (as.numeric(dfRelation$V6))+1
dfFriends = read.csv(file = 'results/friend-valentines', header = FALSE)
dfFriends = dfFriends + 1

dfAll = dfAll %>% select( 2, 3, 15, 43, 42)

#Change column name
names(dfAll) = c( 'email', 'nombre', 'descripcion', 'tel', 'insta')

###########################################################################################
##########################################################################################

#Friends

      #Get names and emails
fName <- c()
email <-c()
for (i in dfFriends$V1){
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

      #Valentines
val1 <-c()
per1 <-c()
insta1 <-c()
tel1 <- c()
desc1 <-c()
val2 <-c()
per2 <-c()
insta2 <-c()
tel2 <- c()
desc2 <-c()
val3 <-c()
per3 <-c()
insta3 <-c()
tel3 <- c()
desc3 <-c()
val4 <-c()
per4 <-c()
insta4 <-c()
tel4 <- c()
desc4 <-c()

for (i in dfFriends$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}

for (i in dfFriends$V3){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}


for (i in dfFriends$V4){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}

for (i in dfFriends$V5){
  val4 = c(val4, dfAll$nombre[i])
  insta4 = c(insta4, dfAll$insta[i])
  tel4 = c(tel4, dfAll$tel[i])
  desc4 = c(desc4, dfAll$descripcion[i])
}

#Escribir nombres e emails

for (i in dfFriends$V2){
  #print(name[i])
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

#Valentines

for (i in dfFriends$V1){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}

for (i in dfFriends$V3){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}


for (i in dfFriends$V4){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}

for (i in dfFriends$V5){
  val4 = c(val4, dfAll$nombre[i])
  insta4 = c(insta4, dfAll$insta[i])
  tel4 = c(tel4, dfAll$tel[i])
  desc4 = c(desc4, dfAll$descripcion[i])
}


      #Get names and emails

for (i in dfFriends$V3){
  #print(name[i])
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

#Valentines

for (i in dfFriends$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}

for (i in dfFriends$V1){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}


for (i in dfFriends$V4){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}

for (i in dfFriends$V5){
  val4 = c(val4, dfAll$nombre[i])
  insta4 = c(insta4, dfAll$insta[i])
  tel4 = c(tel4, dfAll$tel[i])
  desc4 = c(desc4, dfAll$descripcion[i])
}

    #Get names and emails

for (i in dfFriends$V4){
  #print(name[i])
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

#Valentines

for (i in dfFriends$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}

for (i in dfFriends$V3){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}


for (i in dfFriends$V1){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}

for (i in dfFriends$V5){
  val4 = c(val4, dfAll$nombre[i])
  insta4 = c(insta4, dfAll$insta[i])
  tel4 = c(tel4, dfAll$tel[i])
  desc4 = c(desc4, dfAll$descripcion[i])
}

    #Get names and emails

for (i in dfFriends$V5){
  #print(name[i])
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

#Valentines

for (i in dfFriends$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}

for (i in dfFriends$V3){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}


for (i in dfFriends$V4){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}

for (i in dfFriends$V1){
  val4 = c(val4, dfAll$nombre[i])
  insta4 = c(insta4, dfAll$insta[i])
  tel4 = c(tel4, dfAll$tel[i])
  desc4 = c(desc4, dfAll$descripcion[i])
}


    #Building final DF
finalDFFriends <- data.frame(fName, email, val1,  insta1, tel1, desc1, val2,  insta2, tel2, desc2, val3, insta3, tel3, desc3, val4, insta4, tel4, desc4)
names(finalDFFriends) = c('First Name', 'Email', 'Valentine 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2',  'insta2', 'tel2', 'Description 2', 'Valentine 3',  'insta3', 'tel3', 'Description 3','Valentine 4', 'insta4', 'tel4', 'Description 4')

    #Delete NAs in 'First Name'
completeFun <- function(data, desiredCols) {
  completeVec <- complete.cases(data[, desiredCols])
  return(data[completeVec, ])
}

finalDFFriends <- completeFun(finalDFFriends, 'First Name')


write.csv(finalDFFriends,"mail_data//finalDFFriends", row.names = FALSE)

##############################################################################################
##############################################################################################

#Relationship

    #Get names and emails
fName <- c()
email <-c()
for (i in dfRelation$V1){
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

    #Valentines
val1 <-c()
per1 <-c()
insta1 <-c()
tel1 <- c()
desc1 <-c()
val2 <-c()
per2 <-c()
insta2 <-c()
tel2 <- c()
desc2 <-c()
val3 <-c()
per3 <-c()
insta3 <-c()
tel3 <- c()
desc3 <-c()

for (i in dfRelation$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}
per1 = c(dfRelation$V3)

for (i in dfRelation$V4){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}
per2 = dfRelation$V5

for (i in dfRelation$V6){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}
per3 = c(dfRelation$V7)

      #Count matches
allVal1 <-c()
allVal2 <-c()
allVal3 <-c()

for (i in dfRelation$V1){
  myVal = 0
  dfRelation$V2[is.na(dfRelation$V2)]<-0
  for (j in dfRelation$V2){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal1<-c(allVal1, myVal)
}

for (i in dfRelation$V1){
  myVal = 0
  dfRelation$V4[is.na(dfRelation$V4)]<-0
  for (j in dfRelation$V4){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal2<-c(allVal2, myVal)
}

for (i in dfRelation$V1){
  myVal = 0
  dfRelation$V6[is.na(dfRelation$V6)]<-0
  for (j in dfRelation$V6){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal3<-c(allVal3, myVal)
}

myValCont = allVal1+allVal2+allVal3

#Building final DF

finalDFRelation <- data.frame(fName, email, val1, per1, insta1, tel1, desc1, val2, per2, insta2, tel2, desc2, val3, per3, insta3, tel3, desc3, myValCont)
names(finalDFRelation) = c('First Name', 'Email', 'Valentine 1', 'Porcentaje 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2', 'Porcentaje 2', 'insta2', 'tel2', 'Description 2', 'Valentine 3', 'Porcentaje 3', 'insta3', 'tel3', 'Description 3', 'My Valentines')


write.csv(finalDFRelation,"mail_data//finalDFRelation.csv", row.names = FALSE)



#####################################################################################################
######################################################################################################



#Casual

#Get names and emails
fName <- c()
email <-c()
for (i in dfCasual$V1){
  fName <- c(fName, dfAll$nombre[i])
  email <- c(email, dfAll$email[i])
}

val1 <-c()
per1 <-c()
insta1 <-c()
tel1 <- c()
desc1 <-c()
val2 <-c()
per2 <-c()
insta2 <-c()
tel2 <- c()
desc2 <-c()
val3 <-c()
per3 <-c()
insta3 <-c()
tel3 <- c()
desc3 <-c()

for (i in dfCasual$V2){
  val1 = c(val1, dfAll$nombre[i])
  insta1 = c(insta1, dfAll$insta[i])
  tel1 = c(tel1, dfAll$tel[i])
  desc1 = c(desc1, dfAll$descripcion[i])
}
per1 = c(dfCasual$V3)

for (i in dfCasual$V4){
  val2 = c(val2, dfAll$nombre[i])
  insta2 = c(insta2, dfAll$insta[i])
  tel2 = c(tel2, dfAll$tel[i])
  desc2 = c(desc2, dfAll$descripcion[i])
}
per2 = c(dfCasual$V5)

for (i in dfCasual$V6){
  val3 = c(val3, dfAll$nombre[i])
  insta3 = c(insta3, dfAll$insta[i])
  tel3 = c(tel3, dfAll$tel[i])
  desc3 = c(desc3, dfAll$descripcion[i])
}
per3 = c(dfCasual$V7)

#Count matches
allVal1 <-c()
allVal2 <-c()
allVal3 <-c()

for (i in dfCasual$V1){
  myVal = 0
  dfCasual$V2[is.na(dfCasual$V2)]<-0
  for (j in dfCasual$V2){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal1<-c(allVal1, myVal)
}

for (i in dfCasual$V1){
  myVal = 0
  dfCasual$V4[is.na(dfCasual$V4)]<-0
  for (j in dfCasual$V4){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal2<-c(allVal2, myVal)
}

for (i in dfCasual$V1){
  myVal = 0
  dfCasual$V6[is.na(dfCasual$V6)]<-0
  for (j in dfCasual$V6){
    if (i == j){
      myVal = myVal +1
    }
  }
  allVal3<-c(allVal3, myVal)
}

myValCont = allVal1+allVal2+allVal3

#Building final DF
finalDFCasual <- data.frame(fName, email, val1, per1, insta1, tel1, desc1, val2, per2, insta2, tel2, desc2, val3, per3, insta3, tel3, desc3, myValCont)
names(finalDFCasual) = c('First Name', 'Email', 'Valentine 1', 'Porcentaje 1', 'insta1', 'tel1', 'Description 1', 'Valentine 2', 'Porcentaje 2', 'insta2', 'tel2', 'Description 2', 'Valentine 3', 'Porcentaje 3', 'insta3', 'tel3', 'Description 3', 'My Valentines')

write.csv(finalDFCasual,"mail_data\\finalDFCasual.csv", row.names = FALSE)
