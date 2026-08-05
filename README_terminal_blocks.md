# my-docker-workstation

## 1. 로컬 작업 폴더 만들기

- 실제로는 먼저 깃허브에서 레포를 만들고 vs code에서 clone 하고 작업 진행
- 연습을 위해 폴더를 따로 만들고 연습했음.

![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/making%20files.png)

입력

```bash
cd ..
mkdir my-docker-workstation-git-practice
cd my-docker-workstation-git-practice
mkdir screenshots
mkdir static
mkdir template
touch .gitignore
touch Dockerfile
touch README.md
```

출력

```text
출력 없음
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/making%20files%20at%20specific%20folders.png)

입력

```bash
cd static
touch style.css
cd ..
cd template
touch index.html
cd ..
pwd
```

출력

```text
/Users/etd937285/codyssey_mission1/my-docker-workstation-git-practice
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/git%20init.png)

입력

```bash
cd my-docker-workstation-git-practice
git init
```

출력

```text
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to 'main' in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:     git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:     git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /Users/etd937285/codyssey_mission1/my-docker-workstation-git-practice/.git/
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/check%20files.png)

입력

```bash
ls -la
```

출력

```text
total 0
drwxr-xr-x  9 etd937285  etd937285  288  8  5 13:09 .
drwxr-xr-x  5 etd937285  etd937285  160  8  5 13:08 ..
drwxr-xr-x  9 etd937285  etd937285  288  8  5 13:09 .git
-rw-r--r--  1 etd937285  etd937285    0  8  5 12:58 .gitignore
-rw-r--r--  1 etd937285  etd937285    0  8  5 12:59 Dockerfile
-rw-r--r--  1 etd937285  etd937285    0  8  5 12:59 README.md
drwxr-xr-x  2 etd937285  etd937285   64  8  5 12:58 screenshots
drwxr-xr-x  3 etd937285  etd937285   96  8  5 13:10 static
drwxr-xr-x  3 etd937285  etd937285   96  8  5 13:10 template
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/localworkfolder.png)

입력

```bash
ls -la
```

출력

```text
total 24
drwxr-xr-x  10 etd937285  etd937285   320  8  5 14:59 .
drwxr-xr-x   5 etd937285  etd937285   160  8  5 13:08 ..
-rw-r--r--@  1 etd937285  etd937285  6148  8  5 14:11 .DS_Store
drwxr-xr-x  10 etd937285  etd937285   320  8  5 13:50 .git
-rw-r--r--   1 etd937285  etd937285     0  8  5 12:58 .gitignore
-rw-r--r--   1 etd937285  etd937285     0  8  5 12:59 Dockerfile
-rwxr-xr-x   1 etd937285  etd937285    22  8  5 14:54 README.md
drwxr-xr-x   2 etd937285  etd937285    64  8  5 12:58 screenshots
drwxr-xr-x   3 etd937285  etd937285    96  8  5 13:10 static
drwxr-xr-x   3 etd937285  etd937285    96  8  5 13:10 template
```
## 2. 실행 환경 정보 확인

- os, 쉡 종류 및 버전, 터미널 종류, docker, git 버전 확인

![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/os%20version%20check.png)

입력

```bash
sw_vers
```

출력

```text
ProductName:            macOS
ProductVersion:         15.7.4
BuildVersion:           24G517
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/shell%20check.png)

입력

```bash
zsh --version
bash --version
```

출력

```text
zsh 5.9 (x86_64-apple-darwin24.0)
GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin24)
Copyright (C) 2007 Free Software Foundation, Inc.
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/terminal%20check.png)

입력

```bash
echo $TERM_PROGRAM
```

출력

```text
vscode
```
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/vscodeversion.png)

입력

```bash
code --version
```

출력

```text
1.112.0
07ff9d6178ede9a1bd12ad3399074d726ebe6e43
x64
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerversion.png)

입력

```bash
docker --version
```

출력

```text
Docker version 28.5.2, build ecc6942
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/git%20version%20check.png)

입력

```bash
git --version
```

출력

```text
git version 2.53.0
```

## 3. 터미널 기본 조작 실습

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/pwd.png)

입력

```bash
pwd
ls
ls -la
```

출력

```text
/Users/etd937285/codyssey_mission1/my-docker-workstation
Dockerfile  LEARNING_FROM_MISSION1.md  README.md  screenshots  static  templates

디렉터리의 상세 목록이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/cpmvcat.png)

입력

```bash
echo "README write practice" > README.md
cat README.md
cp README.md README22.md
cat README22.md
mkdir movePractice
mv README22.md /movePractice
cd movePractice
ls
ls -la
mv README22.md movePractice
cd ..
mv README22.md movePractice
cd movePractice
ls
```

출력

```text
README write practice
README write practice
mv: fastcopy: open() failed (to): /movePractice: Read-only file system
total 0
drwxr-xr-x  2 etd937285  etd937285  64  8  5 14:55 .
drwxr-xr-x 12 etd937285  etd937285 384  8  5 14:55 ..
mv: rename README22.md to movePractice: No such file or directory
README22.md
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/remove.png)

입력

```bash
rm README22.md
ls
ls -a
```

출력

```text
.  ..
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/rmdir.png)

입력

```bash
rmdir movePractice
ls -la
```

출력

```text
movePractice 디렉터리가 삭제된 뒤 현재 디렉터리의 상세 목록이 출력됨
```

## 4. 파일과 디렉토리 권한 변경 실습

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/permissionpractice.png)

입력

```bash
ls -la
chmod 755 README.md
ls -la
```

출력

```text
README.md 권한이 -rw-r--r--에서 -rwxr-xr-x로 변경됨
```

## 5. Docker 설치 및 데몬 동작 확인, 현재 깔려있는 이미지 및 컨테이너 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerversion.png)

입력

```bash
docker --version
```

출력

```text
Docker version 28.5.2, build ecc6942
```

```
etd937285@c4r3s4 my-docker-workstation % docker info
... 생략

Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/etd937285/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/etd937285/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
 Storage Driver: overlay2

 CPUs: 6
 Total Memory: 15.67GiB
 ... 생략
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerps1.png)

입력

```bash
docker ps
```

출력

```text
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerps_a.png)

입력

```bash
docker ps -a
```

출력

```text
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerimages1.png)

입력

```bash
docker images
```

출력

```text
REPOSITORY   TAG   IMAGE ID   CREATED   SIZE
```

## 6. hello-world 컨테이너 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/hellotest.png)

입력

```bash
docker run --name hello-test hello-world
```

출력

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
Digest: sha256:c3cbe1cc1aa588a64951ac6286e0df7b27fe2e6324b1001c619bb358770c0178
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/hellotestdockerps_a.png)

입력

```bash
docker ps -a
```

출력

```text
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS   NAMES
4ff472e03e48   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago           hello-test
```

## 7. Ubuntu 컨테이너 실행 및 내부 진입

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntutest.png)

입력

```bash
docker run -it --name ubuntu-test ubuntu bash
```

출력

```text
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
0d819469700f: Pull complete
a3679419df18: Pull complete
Digest: sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb
Status: Downloaded newer image for ubuntu:latest
root@b1ee529fac8a:/#
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntutestpwd.png)

입력

```bash
pwd
ls -la
```

출력

```text
/

루트 디렉터리의 파일과 디렉터리 목록이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntuechocat.png)

입력

```bash
echo "hello ubuntu" > test.txt
cat test.txt
```

출력

```text
hello ubuntu
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntudockerps_a1.png)

입력

```bash
docker ps -a
```

출력

```text
ubuntu-test 컨테이너가 종료된 상태로 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntustart1.png)

입력

```bash
docker start ubuntu-test
```

출력

```text
ubuntu-test
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntudockerexec.png)

입력

```bash
docker exec -it ubuntu-test bash
```

출력

```text
root@b1ee529fac8a:/#
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntuexec.png)

입력

```bash
cat test.txt
```

출력

```text
hello ubuntu
```


## 8. NGINX 기본 이미지 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultimage.png)

입력

```bash
docker pull nginx:alpine
```

출력

```text
nginx:alpine 이미지 다운로드가 완료됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerimages2.png)

입력

```bash
docker images
```

출력

```text
nginx:alpine, ubuntu:latest, hello-world:latest 이미지 목록이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultcontainer.png)

입력

```bash
docker run -d --name nginx-default -p 8080:80 nginx:alpine
```

출력

```text
NGINX 컨테이너 ID가 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultcontainer8080.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/curlhttp.png)

입력

```bash
curl http://localhost:8080
```

출력

```text
NGINX 기본 Welcome 페이지의 HTML이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultstoprm.png)

입력

```bash
docker stop nginx-default
docker rm nginx-default
```

출력

```text
nginx-default
nginx-default
```

## 9. 정적 페이지 작성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Workstation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main class="container">
        <h1>Docker Workstation</h1>
        <p>NGINX 컨테이너에서 실행 중인 정적 웹페이지입니다.</p>

        <section>
            <h2>사용한 기술</h2>
            <ul>
                <li>Docker</li>
                <li>NGINX</li>
                <li>HTML/CSS</li>
            </ul>
        </section>
    </main>
</body>
</html>
```

## 10. Dockerfile 작성

```dockerfile
FROM nginx:alpine

LABEL org.opencontainers.image.title="my-docker-workstation"
LABEL org.opencontainers.image.description="Week 1 custom NGINX static website docker practice"

COPY templates/ /usr/share/nginx/html/

EXPOSE 80
```

## 11. 커스텀 이미지 빌드

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagebuild.png)

입력

```bash
docker build -t my-web:1.0 .
```

출력

```text
Dockerfile을 사용해 my-web:1.0 이미지 빌드가 완료됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagebuilddockerimage.png)

입력

```bash
docker images
```

출력

```text
my-web   1.0 이미지가 목록에 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect1.png)

입력

```bash
docker inspect my-web:1.0
```

출력

```text
my-web:1.0 이미지의 상세 JSON 정보가 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect2.png)

입력

```bash
docker inspect my-web:1.0
```

출력

```text
Config, Labels, ExposedPorts 등 이미지 상세 정보가 출력됨
```

## 12. 커스텀 이미지 컨테이너 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer.png)

입력

```bash
docker run -d --name my-web-container -p 8080:80 my-web:1.0
```

출력

```text
커스텀 이미지 컨테이너 ID가 출력됨
```

## 13. 포트 매핑 검증

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainercurl.png)

입력

```bash
curl http://localhost:8080
```

출력

```text
작성한 Docker Workstation 정적 페이지의 HTML이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer8080.png)

## 14. 컨테이너 로그 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer8080log.png)

입력

```bash
docker logs my-web-container
```

출력

```text
NGINX 시작 로그와 HTTP GET 요청 로그가 출력됨
```

## 15. 컨테이너 리소스 사용량 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerstats.png)

입력

```bash
docker stats --no-stream
```

출력

```text
CONTAINER ID   NAME               CPU %   MEM USAGE / LIMIT   MEM %   NET I/O   BLOCK I/O   PIDS
컨테이너의 리소스 사용량이 출력됨
```

## 16. 컨테이너 내부에 실제로 복사가 되었는지 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck1.png)

입력

```bash
docker exec -it my-web-container sh
```

출력

```text
/ #
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck2.png)

입력

```bash
cd /usr/share/nginx/html
ls -la
```

출력

```text
index.html과 style.css가 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy3.png)

입력

```bash
cat index.html
```

출력

```text
컨테이너에 복사된 index.html 내용이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy4.png)

입력

```bash
cat style.css
```

출력

```text
컨테이너에 복사된 style.css 내용이 출력됨
```

## 17. 이미지와 컨테이너 분리 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimageandcontainer.png)

입력

```bash
docker images
docker ps -a
```

출력

```text
my-web:1.0 이미지와 해당 이미지로 실행한 컨테이너가 각각 별도로 출력됨
```

## 18. 바인드 마운트 검증

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount1.png)

입력

```bash
docker run -d --name bind-web -p 8082:80 -v "$(pwd)/static:/usr/share/nginx/html:ro" nginx:alpine
```

출력

```text
바인드 마운트 컨테이너 ID가 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount2.png)

입력

```bash
curl http://localhost:8082
```

출력

```text
호스트 static 디렉터리의 정적 페이지 HTML이 출력됨
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount3.png)

입력

```bash
echo "bind mount test" >> static/index.html
```

출력

```text
출력 없음
```
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount4.png)

입력

```bash
curl http://localhost:8082
```

출력

```text
호스트에서 변경한 내용이 반영된 HTML이 출력됨
```


## 19. Docker 볼륨 생성 

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/volumecreate.png)

입력

```bash
docker volume create workstation-data
```

출력

```text
workstation-data
```

## 20. 첫 번째 컨테이너에서 볼륨에 데이터 저장


![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/firstcontainerstore.png)

입력

```bash
docker run -d --name vol-test -v workstation-data:/data ubuntu sleep infinity
docker exec vol-test sh -c 'echo "volume persistence test" > /data/test.txt'
docker exec vol-test cat /data/test.txt
```

출력

```text
volume persistence test
```

## 21. 첫 번째 컨테이너 삭제


![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/firstcontainerdelete.png)

입력

```bash
docker rm -f vol-test
```

출력

```text
vol-test
```

## 22. 새 컨테이너에서 기존 데이터 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/newcontainerdatacheck.png)

입력

```bash
docker run --rm -v workstation-data:/data ubuntu cat /data/test.txt
```

출력

```text
volume persistence test
```
