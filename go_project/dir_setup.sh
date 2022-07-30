FOLDER=$1
PROJECT_NAME=$2

mkdir $FOLDER/internal
mkdir $FOLDER/cmd
cp Makefile $FOLDER/Makefile
cp .gitignore $FOLDER/.gitignore
cp Dockerfile $FOLDER/Dockerfile
cp -r .github $FOLDER/.github
cp .env $FOLDER/.env

cd $FOLDER/cmd
go mod init $PROJECT_NAME
go mod tidy
go mod vendor


