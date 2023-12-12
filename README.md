# COMPRA AHORRA

## CREACION IMAGEN
Para crear una imagen mediante dockerfile deberemos ejecutar el sigueinte comando


docker build -t compra_ahorra_img:0.0.1 .
## CREACION CONTENEDOR

para crear un contenedor a partir de la imagen anteriormente creada se debe ejecutar el siguiente comando.

docker run -d -p 9000:9000 --name compra_ahorra_container compra_ahorra_img:0.0.1 