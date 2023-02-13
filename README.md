# Deduplication Project
### Deduplication Project Milvus Requirements

- 3 containers
  - milvus
  - etcd
  - minio
- All of them will running on ECS
- Milvus container needs Network Load Balancer because its runs gRPC server
  - gRPC Port: 19530
- up to 50 GB EBS Disk must be mounted to milvus container on this path: https://github.com/acikkaynak/deduplication/blob/f61cbcda8befb0847ae32bc30084eac5663be4a9/milvus/docker-compose.yml#L43


### Deduplication Project Architecture

![image](https://user-images.githubusercontent.com/20394555/218554876-1dee9de1-865f-40b4-826e-aa1cd6661ea5.png)
  

  
