# my-docker-workstation

## 1. 로컬 작업 폴더 만들기

- 실제로는 먼저 깃허브에서 레포를 만들고 vs code에서 clone 하고 작업 진행
- 연습을 위해 폴더를 따로 만들고 연습했음.

![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/making%20files.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/making%20files%20at%20specific%20folders.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/git%20init.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/check%20files.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/localworkfolder.png)
## 2. 실행 환경 정보 확인

- os, 쉡 종류 및 버전, 터미널 종류, docker, git 버전 확인

![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/os%20version%20check.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/shell%20check.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/terminal%20check.png)
![making files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/vscodeversion.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerversion.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/git%20version%20check.png)

## 3. 터미널 기본 조작 실습

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/pwd.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/cpmvcat.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/remove.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/rmdir.png)

## 4. 파일과 디렉토리 권한 변경 실습

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/permissionpractice.png)

## 5. Docker 설치 및 데몬 동작 확인, 현재 깔려있는 이미지 및 컨테이너 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerversion.png)

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
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerps_a.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerimages1.png)

## 6. hello-world 컨테이너 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/hellotest.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/hellotestdockerps_a.png)

## 7. Ubuntu 컨테이너 실행 및 내부 진입

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntutest.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntutestpwd.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntuechocat.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntudockerps_a1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntustart1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntudockerexec.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/ubuntuexec.png)
