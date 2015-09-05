alias ll='ls -lG'
alias f='open -a Finder ./'
alias which='type -all'
gitclean() {
    git reset
    git checkout .
    git clean -fx
    git status
}
dockubuntu() {
  docker-machine start default
  eval "$(docker-machine env default)"
  docker run -it ubuntu bash
}
dockrm(){
  docker stop $1
  docker rm $1
}
dockip() {
  docker-machine ip default
}
dockps() {
  docker ps -a
}
dockreset() {
    docker-machine regenerate-certs default
    docker-machine restart default
}
itrun() {
  sbt it:test
}
itcompile() {
  sbt it:compile
}
sbt-full() {
    sbt clean update compile test jacoco:cover
    itup
    sbt it:test
    itdown
}
java-home () {
  export JAVA_HOME=`/usr/libexec/java_home $@`
  echo "JAVA_HOME:" $JAVA_HOME
  echo "java -version:"
  java -version
}
editbash() {
  atom ~/.bash_profile
}
