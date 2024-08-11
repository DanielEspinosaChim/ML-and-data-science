# importar el dataset 
df <- read.csv('D:/PruebasMLUd/Data.csv')

# tratamiento de los valores desconocidos 

df$Age <- ifelse(is.na(df$Age), ave(df$Age, FUN = function(x) mean(x, na.rm = TRUE)), df$Age)

df$Salary <- ifelse(is.na(df$Salary), ave(df$Salary, FUN = function(x) mean(x, na.rm = TRUE)), df$Salary)

# para acceder a posiciones en R es con el signo de moneda $ 
# el ifelse aqui se hace mediante tres separaciones por comas de lo que este entre los parentesis (,,) 
# donde la primera seccion es la condicion, la seccion del medio es lo que se hara en este caso del if y el lado izquierdo es el else
# el is.na(df$Salary) evalua si hay nan en esa columna 
# ave genera un subconjunto de los valores de x y promediarlos
# ave(df$Salary, FUN = function(x) mean(x, na.rm = TRUE)) esto sirve para remplazar todos los valores de la columna seleccionada 
# que esten en nan por la media de los valores del subconjunto sin contar los nans
# la ultima condicion indica que si no hay na mantenga el valor que tenia antes 

# codificar las variables categoricas 
df$Country <- factor(df$Country, levels = c("France", "Spain", "Germany"), labels = c(1, 2, 3))
# basicamente en R lo haces a mano, levels es que de el df en la columna que seleccionaste tiene que mapear con el numero que le pases en esa posicion

df$Purchased <- factor(df$Purchased, levels = c("No", "Yes"), labels = c(0, 1))

# dividir los datos en conjunto de entrenamiento y test
# install.packages("caTools")  asi se instalan paquetes o librerias en R 
library(caTools) # asi cargas la libreria por codigo 
set.seed(42)
split <- sample.split(df$Purchased, SplitRatio = 0.8)

training_set <- subset(df, split == TRUE) 
testing_set <- subset(df, split == FALSE)

