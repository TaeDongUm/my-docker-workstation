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


## 8. NGINX 기본 이미지 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultimage.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerimages2.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultcontainer.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultcontainer8080.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/curlhttp.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/nginxdefaultstoprm.png)

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
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagebuilddockerimage.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerinspect2.png)

## 12. 커스텀 이미지 컨테이너 실행

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer.png)

## 13. 포트 매핑 검증

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainercurl.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer8080.png)

## 14. 컨테이너 로그 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimagecontainer8080log.png)

## 15. 컨테이너 리소스 사용량 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/dockerstats.png)

## 16. 컨테이너 내부에 실제로 복사가 되었는지 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopycheck2.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy3.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/custombuildfilecopy4.png)

## 17. 이미지와 컨테이너 분리 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/customimageandcontainer.png)

## 18. 바인드 마운트 검증

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount1.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount2.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount3.png)
![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/bindmount4.png)


## 19. Docker 볼륨 생성 

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/volumecreate.png)

## 20. 첫 번째 컨테이너에서 볼륨에 데이터 저장


![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/firstcontainerstore.png)

## 21. 첫 번째 컨테이너 삭제


![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/firstcontainerdelete.png)

## 22. 새 컨테이너에서 기존 데이터 확인

![image files](https://github.com/TaeDongUm/my-docker-workstation/blob/main/screenshots/newcontainerdatacheck.png)
