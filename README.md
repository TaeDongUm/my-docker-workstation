# my-docker-workstation

# 프로젝트 개요

1. 프로젝트 개요

이 프로젝트는 리눅스 CLI, Docker, Git/GitHub를 사용해 재현 가능한 개발 워크스테이션을 구축하는 진행한 과정을 담았습니다.

터미널에서 파일과 디렉터리를 생성, 이동, 복사, 삭제하고 권한을 변경하면서 기본적인 CLI 사용법을 익혔습니다. 이후 OrbStack을 통해 Docker 엔진을 실행하고, Docker 이미지와 컨테이너를 생성하고 관리하는 과정을 실습했습니다.

nginx:alpine 이미지를 베이스 이미지로 선택하여 HTML/CSS 정적 페이지가 포함된 커스텀 Docker 이미지를 제작했습니다. Dockerfile로 이미지를 빌드한 뒤 컨테이너를 실행하고, 호스트의 8080 포트와 컨테이너의 80 포트를 연결하여 브라우저와 curl 명령으로 접속을 검증했습니다.

또한 바인드 마운트를 통해 호스트 파일의 변경 내용이 실행 중인 컨테이너에 즉시 반영되는 것을 확인했습니다. Docker 볼륨 실습에서는 첫 번째 컨테이너에서 생성한 데이터를 컨테이너 삭제 후 새로운 컨테이너에서도 확인하여 데이터 영속성을 검증했습니다.

마지막으로 Git 사용자 정보와 기본 브랜치를 설정하고, 로컬 저장소를 GitHub 원격 저장소와 연결하여 실습 결과와 문서를 관리했습니다.

# 수행 항목 체크리스트

## 터미널 및 실행 환경

- [x] 현재 작업 경로를 확인했다.
- [x] 일반 파일과 숨김 파일을 포함한 디렉터리 목록을 확인했다.
- [x] 파일과 디렉터리를 생성했다.
- [x] 파일을 복사했다.
- [x] 파일을 이동하거나 이름을 변경했다.
- [x] 파일과 디렉터리를 삭제했다.
- [x] cat 명령으로 파일 내용을 확인했다.
- [x] touch 명령으로 빈 파일을 생성했다.
- [x] OS, Shell, Terminal, VS Code 버전을 확인했다.
- [x] Docker와 Git 버전을 확인했다.

파일 및 디렉터리 권한

- [x] 파일의 기존 권한을 확인했다.
- [x] chmod 명령으로 파일 권한을 변경했다.
- [x] 파일 권한 변경 전후를 비교했다.
- [x] 디렉터리의 권한을 변경하고 변경 전후를 비교했다.
- [x] 755, 644와 rwx 권한의 관계를 README에 설명했다.

Docker 설치 및 기본 점검

- [x] OrbStack을 통해 Docker 엔진을 실행했다.
- [x] docker --version으로 Docker CLI 설치 상태를 확인했다.
- [x] docker info로 Docker 엔진 동작 상태를 확인했다.
- [x] docker images로 이미지 목록을 확인했다.
- [x] docker ps로 실행 중인 컨테이너를 확인했다.
- [x] docker ps -a로 종료된 컨테이너를 포함한 목록을 확인했다.
- [x] docker logs로 컨테이너 로그를 확인했다.
- [x] docker stats --no-stream으로 컨테이너 리소스 사용량을 확인했다.

컨테이너 실행

- [x] hello-world 이미지를 내려받고 컨테이너를 실행했다.
- [x] 종료된 hello-world 컨테이너를 docker ps -a로 확인했다.
- [x] Ubuntu 컨테이너를 대화형 모드로 실행했다.
- [x] Ubuntu 컨테이너 내부에서 pwd, ls, echo, cat 명령을 실행했다.
- [x] 종료된 Ubuntu 컨테이너를 다시 시작했다.
- [x] docker exec를 이용해 실행 중인 컨테이너에 접속했다.
- [x] attach와 exec를 각각 실행하고 동작 차이를 정리했다.

Dockerfile 및 커스텀 이미지

- [x] nginx:alpine 베이스 이미지를 선택했다.
- [x] HTML/CSS 정적 웹페이지를 작성했다.
- [x] Dockerfile을 직접 작성했다.
- [x] 정적 페이지를 NGINX 서비스 경로에 복사하도록 설정했다.
- [x] 커스텀 이미지의 제목과 설명을 LABEL로 추가했다.
- [x] 컨테이너가 사용할 80 포트를 명시했다.
- [x] docker build로 my-web:1.0 이미지를 빌드했다.
- [x] docker images로 생성된 이미지를 확인했다.
- [x] docker inspect로 이미지 설정을 확인했다.
- [x] 커스텀 이미지로 컨테이너를 실행했다.
- [x] NGINX 베이스 이미지를 선택한 이유를 README에 설명했다.
- [x] Dockerfile의 각 커스텀 설정과 목적을 README에 설명했다.

포트 매핑 및 웹 접속

- [x] 호스트 8080 포트와 컨테이너 80 포트를 연결했다.
- [x] curl을 이용해 정적 페이지 응답을 확인했다.
- [x] 브라우저에서 정적 페이지 접속을 확인했다.
- [x] 포트가 포함된 브라우저 주소창과 응답 화면을 캡처했다.
- [x] 포트 매핑이 필요한 이유를 README에 설명했다.

바인드 마운트

- [x] 호스트 디렉터리를 NGINX 컨테이너에 바인드 마운트했다.
- [x] 바인드 마운트 컨테이너를 호스트 8082 포트로 실행했다.
- [x] 호스트 파일을 변경하기 전 웹 응답을 확인했다.
- [x] 호스트 파일을 변경했다.
- [x] 컨테이너 재빌드 없이 변경 내용이 반영되는 것을 확인했다.
- [x] 바인드 마운트의 변경 전후 증거를 저장했다.
- [x] 바인드 마운트가 호스트 경로에 의존한다는 점을 README에 설명했다.

Docker 볼륨

- [x] Docker 볼륨을 생성했다.
- [x] 첫 번째 컨테이너에 볼륨을 연결했다.
- [x] 볼륨에 테스트 데이터를 저장했다.
- [x] 첫 번째 컨테이너를 삭제했다.
- [x] 동일한 볼륨을 새로운 컨테이너에 연결했다.
- [x] 새로운 컨테이너에서 기존 데이터를 확인했다.
- [x] 컨테이너 삭제 후에도 데이터가 유지되는 것을 검증했다.
- [x] Docker 볼륨과 컨테이너 생명주기가 분리되는 이유를 README에 설명했다.

Git 및 GitHub

- [x] Git 저장소를 초기화했다.
- [x] Git 사용자 정보를 설정했다.
- [x] Git 기본 브랜치를 설정했다.
- [x] git config --list --show-origin으로 설정을 확인했다.
- [x] GitHub 공개 저장소를 생성했다.
- [x] 로컬 저장소와 GitHub 원격 저장소를 연결했다.
- [x] VS Code와 GitHub 연동 증거를 저장했다.
- [x] 프로젝트 파일과 수행 결과를 GitHub에 업로드했다.

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
echo "Hello from Ubuntu containter"
cat /etc/os-release
exit
```

출력

```text
Hello from Ubuntu container
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
echo "Entered with docker exec"
```

출력

```text
Entered with docker exec
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
docker stop nginx-original
docker rm nginx-original
```

출력

```text
nginx-original
nginx-original
```

## 9. 정적 페이지 작성

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Docker Workstation</title>
    <link rel="stylesheet" href="style.css" />
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
my-static-web   1.0 이미지가 목록에 출력됨
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect1.png)

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect2.png)

입력

```bash
docker inspect my-web:1.0
```

출력

```text
my-web:1.0 이미지의 상세 JSON 정보가 출력됨
```

## 12. 커스텀 이미지 컨테이너 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer.png)

입력

```bash
docker run -d --name my-static-web-8080 -p 8080:80 my-web:1.0
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
docker logs my-static-web-8080
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

- **--no-stream** 은 해당 명령어가 실행될 때 현재 시점의 정지된 스냅샷을 보여줌
- **docker stats** 는 실시간으로 일정 시간마다 계속 감시
  - 프로그램이 종료되지 않고 무한 대기 상태에 빠진다.

출력

```text
CONTAINER ID   NAME               CPU %   MEM USAGE / LIMIT   MEM %   NET I/O   BLOCK I/O   PIDS
컨테이너의 리소스 사용량이 출력됨
```

## 16. 컨테이너 내부에 실제로 복사가 되었는지 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck1.png)

입력

```bash
docker run -d --name my-static-web-8081 -p 8081:80 my-static-web:1.0
```

출력

```text
도커 컨테이너 고유 식별 ID 출력
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck2.png)

- 제대로 동작됨을 브라우저를 통해 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy3.png)

입력

```sh
docker exec -it my-static-web-8081 sh

ls -la /usr/share/nignx/html
```

출력

```text
세부 파일들 목록을 숨김 파일 포함해서 상세 정보 보여줌
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy4.png)

입력

```bash
cat /usr/share/nginx/html/index.html
```

출력

```text
컨테이너에 복사된 index.html 내용이 출력됨
```

## 17. 이미지와 컨테이너 분리 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/imagesandcontainerseparation.png)

입력

```bash
docker rm -f my-static-web-8081
docker images
docker ps -a
```

출력

```text
// docker images 결과
REPOSITORY      TAG       IMAGE ID       CREATED              SIZE
my-static-web   1.0       d20ff7a623aa   About a minute ago   62.4MB

// docker ps -a 결과
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## 18. 바인드 마운트 검증

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount1.png)

입력

```bash
curl http://localhost:8082
```

출력

```text
호스트 static 디렉터리의 정적 페이지 HTML이 출력됨
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount2.png)

입력

```bash
docker run -d --name bind-web -p 8082:80 -v "$(pwd)/static:/usr/share/nginx/html:ro" nginx:alpine
```

출력

```text
바인드 마운트 컨테이너 ID가 출력됨
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount3.png)

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
docker run -d --name vol-test-1 -v workstation-data:/data ubuntu sleep infinity
docker exec vol-test-1 sh -c 'echo "volume persistence test" > /data/message.txt'
docker exec vol-test-1 cat /data/message.txt
```

출력

```text
volume persistence test
```

## 21. 첫 번째 컨테이너 삭제

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/firstcontainerdelete.png)

입력

```bash
docker rm -f vol-test-1
```

출력

```text
vol-test-1
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

## 23. attach vs exec

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/attach%20exit.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/attach%20exit1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/docker%20start.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/execexit.png)

## 24. git 사용자 정보/ 기본 브랜치 설정 후 확인

- `git config --list --show-origin`
- 코디세이 맥 환경이 아닌 집 데스크 탑에서 확인하다보니 여러 설정값들이 보여서 origin으로 어디 파일의 환경설정값인지 확인하였음.

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/gitconfiglist1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/gitconfiglist2.png)

입력

```bash
git config --global user.name "TaeDongUm"
git config --global user.email "etd93@naver.com"
git config --global init.defaultBranch main
git config --list
```

출력

```text
user.name=TaeDongUm
user.email=etd93@naver.com
...
(생략)
init.defaultbranch=main
```

## 25. GitHub 연동 증거

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/git_connect.png)

입력

```bash
git remote -v
```

출력

```text
origin  https://github.com/TaeDongUm/my-docker-workstation.git (fetch)
origin  https://github.com/TaeDongUm/my-docker-workstation.git (push)
```

입력

```bash
git branch --show-current
```

출력

```text
main
```

입력

```bash
git status
```

출력

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## 개념 정리

### 1. 파일 권한 755, 644와 rwx의 관계

| 리눅스의 파일 권한은 다음 세 가지로 구성되어 있음.

- r: 파일을 읽을 수 있는 권한임.
- w: 파일 내용을 수정하거나 삭제할 수 있는 권한임.
- x: 파일을 실행할 수 있는 권한임.

| 각 권한에는 숫자가 정해져 있음.

- r = 4
- w = 2
- x = 1

| 필요한 권한의 숫자를 더해 하나의 권한 값으로 표현함.
| 예를 들어 7은 4 + 2 + 1이므로 읽기, 쓰기, 실행 권한을 모두 가진 상태임.

| 권한 숫자 세 자리는 순서대로 다음 사용자를 의미함.

- 1.파일 소유자
- 2.파일이 속한 그룹
- 3.그 외 사용자

| 755는 다음과 같은 의미가 있음.

- 소유자: 읽기, 쓰기, 실행 가능함.
- 그룹: 읽기, 실행 가능함.
- 그 외 사용자: 읽기, 실행 가능함.

| 문자로 표현하면 rwxr-xr-x임.
| 644는 다음과 같은 의미가 있음.

- 소유자: 읽기, 쓰기 가능함.
- 그룹: 읽기만 가능함.
- 그 외 사용자: 읽기만 가능함.

문자로 표현하면 rw-r--r--임.

### 2. exec vs attach

| exec와 attach는 둘다 컨테이너에 접속하는 명령어

- 둘다 컨테이너가 실행되고 있을 때 사용할 수 있으며, 만약 docker ps 를 입력했을 때 실행 중인 컨테이너가 없다면 실행할 수가 없으므로 새롭게 컨테이너를 실행시키든, 죽은 컨테이너를 살리든 하는 형태로 진행해야만 한다.

#### 1. 한 줄 개념 요약

- **`docker attach`**: 이미 켜져서 돌고 있는 메인 프로그램(PID 1)의 **모니터 화면에 그대로 붙어서 감상/조작하는 것**임.
- **`docker exec`**: 메인 프로그램과 별개로, 컨테이너라는 공간 안에 **새로운 터미널(쉘) 창을 하나 뚫고 들어가는 것**임.

---

#### 2. 왜 `exec`를 훨씬 많이 쓸까?

| 비교 항목          | `docker attach`                                                  | `docker exec`                                     |
| ------------------ | ---------------------------------------------------------------- | ------------------------------------------------- |
| **진입 대상**      | 메인 프로세스 (웹서버, DB, 파이썬 등)                            | 새로 띄운 자식 프로세스 (`/bin/bash` 등)          |
| **명령어 입력**    | 메인 프로세스가 `bash`일 때만 가능함. (웹서버일 땐 입력 안 먹힘) | 어떤 컨테이너든 **항상 명령어 입력 창이 열림**    |
| **`exit` 입력 시** | **컨테이너 전체가 꺼져버림** (매우 위험함)                       | 내 작업창만 닫히고 **컨테이너는 무사함** (안전함) |
| **주요 용도**      | 실시간 출력 화면(로그) 그대로 들여다볼 때                        | 내부 디버깅, 파일 수정, 명령어 실행할 때          |

---

#### 3. 생각해본 질문들

- **`exec`로 들어가서 파일 바꾸면 날아가나?**
- **절대 안 날아감.** `exec`는 새 프로세스(뇌)를 띄운 것일 뿐, 파일 시스템(디스크)은 컨테이너 전체가 공유함. 자식 창에서 파일을 고치면 부모 프로그램에도 바로 적용됨.

- **`exec`는 메인 프로그램을 중복해서 또 켜는 건가?**
- **아님.** 똑같은 웹서버를 하나 더 돌리는 게 아니라, 내부를 만질 수 있는 **'터미널 쉘(bash)' 하나만 달랑 띄우는 것**임.

- **`attach`는 왜 명령어 전달이 안 되나?**
- 메인 프로세스가 `python app.py`나 `nginx`라면, 명령어를 해석해 줄 '쉘'이 켜져 있지 않기 때문임. 내 입력이 쉘이 아닌 파이썬 프로그램으로 전달되어 무시당함.

---

> ** 결론:**
> 실수로 서버를 꺼뜨릴 위험이 없어서 보통의 경우 **`docker exec -it <컨테이너> bash`를 씀**.

### 3. nginx:alpine 베이스 이미지를 선택한 이유

- 커스텀 웹 서버 이미지를 만들기 위한 베이스 이미지로 nginx:alpine을 선택했음.
- NGINX는 정적 HTML, CSS 파일을 웹 브라우저에 제공하는 웹 서버임.
- nginx:alpine 이미지에는 NGINX가 이미 설치되어 있고 기본 실행 설정도 포함되어 있음.
- 따라서 Ubuntu와 같은 일반 Linux 이미지에 NGINX를 직접 설치하는 과정을 생략할 수 있음.
- 이미지 크기가 비교적 작기 때문에 다운로드와 빌드가 빠르고, 간단한 정적 웹 서버를 실행하기에 적합함.

- 이번 프로젝트의 목적은 웹 서버 프로그램을 직접 설치하는 것이 아니라 다음 과정을 확인하는 것이었음.

```text
Dockerfile 작성
커스텀 이미지 빌드
컨테이너 실행
포트 매핑
웹페이지 접속
```

| 따라서 NGINX가 미리 설치된 nginx:alpine 이미지를 사용하는 것이 실습 목적에 적합하다고 판단했음.

### 4. Dockerfile의 각 설정과 목적

- Dockerfile은 커스텀 Docker 이미지를 만들기 위한 설명서 역할을 함.
- 프로젝트에서 사용한 주요 설정의 목적은 다음과 같음.

```dockerfile
FROM
FROM nginx:alpine
```

- 커스텀 이미지의 기반으로 사용할 이미지를 지정함.
- NGINX 웹 서버와 Alpine Linux가 포함된 이미지를 기반으로 사용했음.

```dockerfile
LABEL
LABEL org.opencontainers.image.title="my-custom-nginx"
```

- 이미지에 이름, 설명, 제작자 등의 정보를 추가하기 위한 설정임.
- 이미지 실행에 직접 영향을 주지는 않지만 이미지의 목적과 정보를 확인하기 쉽게 해줌.

```dockerfile
COPY
COPY site/ /usr/share/nginx/html/
```

- 호스트 컴퓨터의 site 디렉터리에 있는 HTML과 CSS 파일을 이미지 내부로 복사함.
- **/usr/share/nginx/html/**은 NGINX가 기본적으로 정적 파일을 제공하는 경로임.
- 이 경로에 파일을 복사했기 때문에 컨테이너를 실행했을 때 직접 만든 웹페이지가 표시됨.

```dockerfile
EXPOSE
EXPOSE 80
```

- 컨테이너 내부에서 웹 서버가 80 포트를 사용한다는 사실을 문서화함.
- EXPOSE 80만 작성한다고 호스트 컴퓨터에서 자동으로 접속할 수 있는 것은 아님.
- 실제 접속을 위해서는 컨테이너 실행 시 -p 옵션으로 포트 매핑을 설정해야 함.

### 5. 포트 매핑이 필요한 이유

- 컨테이너는 호스트 컴퓨터와 분리된 네트워크 환경을 가지고 있음.
- NGINX가 컨테이너 내부의 80 포트에서 실행되고 있어도 호스트 컴퓨터의 브라우저가 해당 포트에 바로 접근할 수 없음.
- 따라서 호스트 컴퓨터의 포트와 컨테이너 내부의 포트를 연결하는 포트 매핑이 필요함.
- 다음 명령으로 포트 매핑을 설정했음.

```bash
docker run -d -p 8080:80 --name my-web-container my-web:1.0
```

- 8080:80은 다음과 같은 의미가 있음.
  - 8080: 호스트 컴퓨터에서 사용하는 포트임.
  - 80: 컨테이너 내부의 NGINX가 사용하는 포트임.

- 브라우저에서 http://localhost:8080으로 요청하면 Docker가 해당 요청을 컨테이너 내부의 80 포트로 전달함.
- 포트 매핑을 사용하면 컨테이너 내부 서비스를 호스트 컴퓨터나 외부 사용자에게 공개할 수 있음.

### 6. 바인드 마운트가 호스트 경로에 의존하는 이유

- 바인드 마운트는 호스트 컴퓨터의 특정 디렉터리를 컨테이너 내부 경로에 직접 연결하는 방식임.
- 다음과 같은 형태로 실행했음.

```bash
docker run -d -p 8082:80 -v "$(pwd)/site:/usr/share/nginx/html:ro" nginx:alpine
```

- 호스트의 site 디렉터리와 컨테이너 내부의 /usr/share/nginx/html 경로가 연결되어 있음.
- 호스트의 HTML 파일을 수정하면 컨테이너를 다시 빌드하지 않아도 변경된 내용이 웹페이지에 반영됨.
- 이는 컨테이너 내부에 파일이 별도로 복사된 것이 아니라, 컨테이너 내부 경로가 호스트 디렉터리의 내용을 직접 바라보고 있기 때문임.
- 바인드 마운트는 호스트의 실제 경로를 직접 사용함.
- 따라서 다른 컴퓨터에서 동일한 명령을 실행할 때 해당 경로가 존재하지 않으면 정상적으로 동작하지 않을 수 있음.

- 예를 들어 다음과 같은 절대 경로를 직접 사용하면 특정 사용자 환경에 의존하게 됨.

```bash
-v /Users/user/project/site:/usr/share/nginx/html
```

- 다른 사용자의 컴퓨터에는 /Users/user/project/site 경로가 없을 수 있음.
- 재현성을 높이기 위해 현재 프로젝트 경로를 나타내는 $(pwd) 또는 상대적인 프로젝트 구조를 사용하는 것이 좋음.

### 7. Docker 볼륨과 컨테이너의 생명주기가 분리되는 이유

- 컨테이너 내부에만 저장된 데이터는 해당 컨테이너를 삭제하면 함께 사라질 수 있음.
- Docker 볼륨은 컨테이너 내부가 아닌 Docker가 별도로 관리하는 저장 공간임.
- 다음 명령으로 볼륨을 생성했음.

```bash
docker volume create mydata
```

- 생성한 볼륨을 컨테이너의 /data 경로에 연결했음.

```bash
docker run -d --name vol-test -v mydata:/data ubuntu sleep infinity
```

- 컨테이너 내부의 /data 경로에 파일을 저장하면 실제 데이터는 mydata 볼륨에 저장됨.
- 컨테이너를 삭제해도 mydata 볼륨은 별도로 남아 있음.
- 새로운 컨테이너에 동일한 볼륨을 연결하면 이전 컨테이너에서 저장한 파일을 다시 확인할 수 있음.
- 컨테이너는 프로그램을 실행하는 공간이고, 볼륨은 데이터를 보관하는 공간으로 역할이 분리되어 있음.
- 이러한 구조를 통해 다음과 같은 장점이 있음.
  - 컨테이너를 삭제하거나 새로 만들어도 데이터를 유지할 수 있음.
  - 새로운 버전의 컨테이너로 교체해도 기존 데이터를 사용할 수 있음.
  - 여러 컨테이너에서 동일한 데이터를 연결해 사용할 수 있음.
  - 애플리케이션 실행 환경과 저장 데이터를 독립적으로 관리할 수 있음.

| 따라서 데이터베이스 파일이나 사용자가 업로드한 파일처럼 계속 보관해야 하는 데이터에는 Docker 볼륨을 사용하는 것이 적합함.

## 트러블슈팅

### 1.

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bug2.png)

- 이름을 헷갈림

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bug2_solution.png)

### 2.

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/cpmvcat.png)

- 절대 경로와 상대경로에 대한 실수

## 추가 보너스 과제

### 1. 보너스 과제 개요

> 기존 미션에서는 _docker run_ 명령으로 컨테이너를 각각 실행했다.
> 보너스 과제에서는 Docker Compose를 사용해서 컨테이너 실행 설정을 _compose.yaml_ 파일로 관리하고 웹 서버와 보조 서비스를 함께 실행했다.
> 커스텀 이미지와 다운 받았던 _nginx:alpine_ 이미지를 재사용해서 좀 더 compose 개념에 익숙해지도록 했다.

```text

최종 구성

브라우저
 ↓
web 서비스
   ↓ Compose 내부 네트워크
helper 서비스

```

- `web` : 기존 정적 웹 페이지를 제공하는 웹 서버
- `helper` : 컨테이너 간 네트워크 통신을 확인하기 위한 보조 웹 서비스

> 웹 서버 1개와 보조 서비스 1개를 구성하여 총 2개의 서비스를 Docker Compose로 함께 실행한다.

---

### 2. 프로젝트 폴더 구성

```text
my-docker-workstation/
├── compose.yaml
├── .env
├── .env.example
├── .gitignore
├── site/
│ └── index.html ├── helper-site/ │ └── index.html ├── screenshots/ └── README.md
```

> 기존 웹 페이지인 templates/index.html와 보조 서비스의 웹 페이지인 helper-templates/index.html를 분리하여 관리했다.
> `helper-templates` 폴더는 보조 서비스가 반환할 정적 페이지를 보관한다.

### 3. 보조 서비스 페이지 작성

```html
<h1>Helper Service Connected</h1>
<p>web 컨테이너에서 helper 서비스로 연결되었습니다.</p>
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/helper_index1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/helper_index2.png)

- 위 응답이 출력되면 `web` 컨테이너에서 `helper` 컨테이너로 HTTP 요청이 정상적으로 전달된 것으로 판단할 수 있다.

### 4. 환경 변수 파일 작성

> 호스트 포트를 Compose 파일에 직접 고정하지 않고 `.env` 파일을 통해 전달했다.

- 이를 통해 Compose 파일이나 웹 페이지 코드를 수정하지 않고도 접속 포트를 변경할 수 있다.
- 또한, 보안을 위해 `.env` 파일은 Git에 올리지 않을 수 있다.
- 대신 다른 사용자가 필요한 환경 변수를 확인할 수 있도록 `.env.example` 파일을 작성했다.
- 이번 미션에서는 크게 문제될 것 같지 않아 둘의 파일을 동일하게 만들었다.

```env
WEB_PORT=8080
```

### 5. Compose 문법 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/dockercomposeconfig.png)

입력

```bash
docker compose config
```

출력

```text
services:
  web:
    container_name: bonus-web
    image: nginx:alpine
    networks:
      default: null
    ports:
      - mode: ingress
        target: 80
        published: "8080"
        protocol: tcp
    volumes:
      - type: bind
        source: \my-docker-workstation\templates
        target: /usr/share/nginx/html
        read_only: true
        bind:
          create_host_path: true
networks:
  default:
    name: my-docker-workstation_default
```

- 포트가 잘 변환되어 보인다.

### 6. 단일 서비스 실행

입력

```bash
docker compose up -d
docker compose ps
docker compose logs web
```

출력

```text
NAME        IMAGE          COMMAND                  SERVICE   CREATED         STATUS         PORTS
bonus-web   nginx:alpine   "/docker-entrypoint.…"   web       3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp

bonus-web  | 172.18.0.1 - - [06/Aug/2026:12:08:04 +0000] "GET / HTTP/1.1" 200 647 ...
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/dockercomposeupd.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/dockercomposeup1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/dockercomposeps.png)

### 7. 멀티 컨테이너로 확장

최종 `compose.yaml`

```compose
services:
  web:
    image: nginx:alpine
    container_name: bonus-web
    ports:
      - "${WEB_PORT}:80"
    volumes:
      - ./templates:/usr/share/nginx/html:ro
    networks:
      - bonus-network

  helper:
    image: nginx:alpine
    container_name: bonus-helper
    volumes:
      - ./helper-templates:/usr/share/nginx/html:ro
    networks:
      - bonus-network

networks:
  bonus-network:
    driver: bridge
```

- 여기서, `helper-templates`의 페이지는 `port`가 없다.
- 즉, 호스트 브라우저에서는 `helper` 에 직접 접근하는 것이 아니다.
- 대신, `Compose 네트워크`에 있는 `web` 컨테이너가 다음 주소로 접근한다.
  - `http://helper`

### 8. 멀티 컨테이너 실행

입력

```bash
docker compose down
```

- 단일 컨테이너 구성 정리하기

입력

```bash

docker compose up -d
docker compose ps
```

출력

```bash
NAME           IMAGE          COMMAND                  SERVICE   CREATED          STATUS         PORTS
bonus-helper   nginx:alpine   "/docker-entrypoint.…"   helper    12 seconds ago   Up 8 seconds   80/tcp
bonus-web      nginx:alpine   "/docker-entrypoint.…"   web       12 seconds ago   Up 8 seconds   0.0.0.0:8080->80/tcp

```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/multidockercomposeps.png)

- 여기서의 차이

```text
web
0.0.0.0:8080->80
호스트에서 접근 가능

helper
80/tcp
Compose 내부 네트워크에서만 접근
```

### 9. 컨테이너 간 네트워크 통신 확인

`web` 컨테이너 안에서 `helper` 서비스로 요청한다.

입력

```bash
docker compose exec web curl http://helper
```

출력

```text
<h1>Helper Service Connected</h1>
<p>web 컨테이너에서 helper 서비스로 연결되었습니다.</p>
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/multidockerexecweb.png)

> 이를 통해 알 수 있는 것

- web과 helper가 같은 compose 네트워크에 연결됨
- web이 helper라는 서비스 이름을 찾고
- compose 네트워크가 helper 서비스의 ip를 반환함
- helper 컨테이너의 80번 포트에 연결됨
- http 응답을 정상적으로 받음

### 10. 네트워크 구조 확인해보기

입력

```bash
docker network ls
docker network inspect <네트워크 이름>
```

출력

```text
f3b7fc3ceef2   my-docker-workstation_bonus-network   bridge    local

--------------------------------------------------------------------------

"Containers": {
    "1b2e41ea61537b8e36067e692fa6374f6bcdf662807458fe0295c23a5dc5ea16": {
        "Name": "bonus-helper",
        "EndpointID": "fff8e68f6a02a08059435b5c0ad4057982e2a65d297b01d3c25d15590e3bc0e4",
        "MacAddress": "9a:e7:57:0d:82:c9",
        "IPv4Address": "172.19.0.2/16",
        "IPv6Address": ""
    },
    "c05dbdeacb2b1d4d2dd1a54fbf7aa51d6f79ecb2ba999f8c64a29772d0fff67d": {
        "Name": "bonus-web",
        "EndpointID": "bf7804d54ab09d7389b47d759a765d4ab3f2ca0d25c4126e777642e6fdb76fca",
        "MacAddress": "fa:b4:70:fc:3e:bf",
        "IPv4Address": "172.19.0.3/16",
        "IPv6Address": ""
    }
},
```

- 하나의 네트워크 안에 2개의 컨테이너가 있으며 서로 다른 내부 IP를 받았다는 의미

### 11. 환경 변수 변경 검증

기존

```env
// .env 파일

WEB_PORT=8080

```

변경 후

```env
// .env 파일

WEB_PORT=8081

```

입력

```bash
docker compose down
docker compose up -d
docker compose ps
```

출력

```text
NAME           IMAGE          COMMAND                  SERVICE   CREATED          STATUS         PORTS
bonus-helper   nginx:alpine   "/docker-entrypoint.…"   helper    10 seconds ago   Up 6 seconds   80/tcp
bonus-web      nginx:alpine   "/docker-entrypoint.…"   web       10 seconds ago   Up 6 seconds   0.0.0.0:8081->80/tcp
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/envfilechange1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/envfilechange.png)

### 12. GitHub SSH 키 설정 과정

#### 1. SSH이란?

> SSH는 Secure Shell의 약자로, 네트워크를 통해 다른 컴퓨터나 서비스에 안전하게 접속하고 인증하는 방식

- GitHub에서는 SSH를 이용해 다음 작업을 할 수 있음

```bash
git clone
git pull
git push
```

- SSH를 설정하면 GitHub에 연결할 때마다 사용자 이름이나 Personal Access Token을 직접 입력하지 않고, 내 컴퓨터에 저장된 SSH 키로 인증할 수 있다.

#### 2. 왜 필요한가?

- GitHub 저장소에 코드를 올리려면 GitHub가 다음을 확인해야 한다.

> 이 요청을 보낸 사람이 정말 이 GitHub 계정의 소유자인가?

- HTTPS 방식에서는 토큰이나 자격 증명 관리자를 사용한다.

```text
내 컴퓨터
   ↓ 아이디·토큰 또는 저장된 자격 증명
GitHub
```

SSH 방식에서는 SSH 키를 사용한다.

```text
내 컴퓨터의 개인키
   ↓ 키를 가지고 있다는 사실 증명
GitHub에 등록된 공개키
```

둘 다 안전한 인증 방식이지만, SSH 방식은 개발 환경에서 다음 장점이 있다.

- 토큰을 매번 직접 입력하지 않아도 된다.
- 컴퓨터별로 키를 따로 만들 수 있다.
- 특정 컴퓨터의 키만 GitHub에서 제거할 수 있다.
- 서버 접속이나 배포 환경에서도 비슷한 키 인증 방식을 사용한다.

#### 3. 키 한 쌍을 사용하는 이유

- SSH 키 방식에서는 GitHub가 개인키를 가지고 있지 않는다.

```text
내 컴퓨터: 개인키
GitHub: 공개키
```

- 인증 과정에서는 개인키 자체를 GitHub에 보내지 않고, 개인키를 실제로 가지고 있다는 사실만 증명한다.

개념적으로는 다음과 같다.

```text
GitHub:
"내가 가지고 있는 공개키와 짝이 되는 개인키를 가지고 있나?"

내 컴퓨터:
"개인키를 공개하지 않고, 그 키를 가지고 있다는 증거를 보냄"

GitHub:
"검증에 성공했으므로 접근을 허용"
```

- 키를 전달하거나 저장하는 과정에서 노출의 위험을 줄인다.

#### 4. SSH 키 비밀번호인 passphrase는 무엇인가?

```text
Enter passphrase (empty for no passphrase):
```

- `passphrase`는 개인키 파일에 거는 추가 비밀번호
- 보안성 증가
- 키를 사용할 때 passphrase 입력 필요
- 편리성을 위해 비워둘 수 있긴 함

#### 5. 설정 절차

---

입력

```bash
ssh -V
```

- SSH 명령 사용 가능 여부 확인

---

입력

```bash
ssh-keygen -h
```

- 공용키/개인키 생성

---

#### 1단계 키 생성

입력

```bash
ssh-keygen -t ed25519 -C "GitHub에 등록된 이메일"
```

- 해당 이메일로 공개키/개인키 생성

---

#### 2단계 키 생성 확인

입력

```bash
ls -la ~/.ssh
```

출력

```text
...(생략)
-rw-r--r-- 1 etd93 197609 411 Aug  6 22:05 id_ed25519
-rw-r--r-- 1 etd93 197609  97 Aug  6 22:05 id_ed25519.pub
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/lslassh.png)

---

#### 3단계 ssh-agent 실행

입력

```bash
eval "$(ssh-agent -s)"
```

출력

```text
Agent pid 1777
```

- 백그라운드 프로그램(ssh-agent)을 실제로 실행시키고 내 터미널 환경에 등록하는 명령어

입력

```bash
ssh-add ~/.ssh/id_ed25519
```

출력

```text
Identity added: ~~~~~~
```

- 생성한 개인키를 등록

---

#### 4단계 공개키 복사

macOS

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

windows

```bash
copy < ~/.ssh/id_ed25519
```

#### 5단계 GitHub에 공개키 등록

```text
프로필 이미지
→ Settings
→ SSH and GPG keys
→ New SSH key
```

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/sshgithub.png)

#### 6단계 GitHub SSH 연결 테스트

```bash
ssh -T git@github.com
```

출력

```text
Hi TaeDongUm! You've successfully authenticated, but GitHub does not provide shell access.
```

#### 7단계 기존 저장소를 SSH 방식으로 변경

입력

```bash
git remote -v
git remote set-url origin git@github.com:TaeDongUm/my-docker-workstation.git
git remote -v
```

출력

```text
origin  git@github.com:TaeDongUm/my-docker-workstation.git (fetch)
origin  git@github.com:TaeDongUm/my-docker-workstation.git (push)
```

#### 8단계 push로 최종 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bonus_mission/sshfinalcheck.png)
