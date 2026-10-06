# 베이스 이미지
FROM quay.io/centos/centos:stream10

# 사용자 추가 및 사용자 확인
RUN ["/usr/sbin/useradd", "user01"]

# USER 지정 전 사용자 확인
RUN ["whoami"]
RUN ["id"]

# 이후 명령 및 컨테이너의 기본 사용자를 user01로 지정
USER user01

# USER 지정 후 사용자 확인
RUN ["whoami"]
RUN ["id"]
