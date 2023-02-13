# Deduplication Project

### Milvus Database Requirements

- 3 Containers
  - **Milvus**:
      - CPU: 4 vCPU
      - Memory: 8 GB
      - Disk: 50 GB (EBS gp3): must be mounted to container on this path:           https://github.com/acikkaynak/deduplication/blob/f61cbcda8befb0847ae32bc30084eac5663be4a9/milvus/docker-compose.yml#L43
  - **etcd**:
      - CPU: 0.5 vCPU
      - Memory: 1 GB
  - **minio**:
      - CPU: 0.5 vCPU
      - Memory: 1 GB
      - S3 Bucket (name: deduplication-milvus-minio-bucket) for remote S3 write
- Running on **EC2**
- **Milvus** needs **Network Load Balancer** because its runs **gRPC** server
  - gRPC Port: 19530

### Deduplication Project Architecture

![image](https://user-images.githubusercontent.com/20394555/218554876-1dee9de1-865f-40b4-826e-aa1cd6661ea5.png)
