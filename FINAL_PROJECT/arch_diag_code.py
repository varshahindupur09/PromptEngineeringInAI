from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.aws.database import RDS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3

# Define the path to the icons
icon_path = "./icons/"

# Create custom nodes for specific icons
airflow_icon = icon_path + "airflow.png"
ml_icon = icon_path + "ml_model.png"
historic_data_icon = icon_path + "historic_data.png"
everyday_data_icon = icon_path + "everyday_data.png"
docker_icon = icon_path + "docker.png"
aws_icon = icon_path + "aws_cloud.png"
terminal_icon = icon_path + "terminal.png"
llm_icon = icon_path + "llm_icon.png"
rag_pipeline_icon = icon_path + "rag_pipeline.jpg"
vector_database_icon = icon_path + "vector_database.png"
embedding_icon = icon_path + "embedding.jpg"

with Diagram("Service Architecture", show=False, direction="TB"):

    with Cluster("JustTogether"):
        airflow = Custom("Airflow", airflow_icon)
        docker = Custom("Docker", docker_icon)

    with Cluster("MLaaS"):
        ml_models = Custom("ML Models", ml_icon)
        llm = Custom("LLM", llm_icon)
        rag_pipeline = Custom("RAG Pipeline", rag_pipeline_icon)
        vector_database = Custom("Vector Database", vector_database_icon)
        embedding = Custom("Embedding", embedding_icon)

    with Cluster("Data As Service"):
        historic_data = Custom("Historic Data", historic_data_icon)
        everyday_data = Custom("Everyday Data", everyday_data_icon)
    
    iam = IAM("IAM")
    rds = RDS("Amazon RDS")
    cloudwatch = Cloudwatch("Cloudwatch")
    aws_cloud = Custom("AWS", aws_icon)
    terminal = Custom("Terminal", terminal_icon)
    s3 = S3("S3")

    with Cluster("Service Cluster"):
        airflow >> docker >> rds >> iam >> cloudwatch

    ml_models >> Edge(label="Data Transfer") >> historic_data
    ml_models >> Edge(label="Data Transfer") >> everyday_data
    llm >> Edge(label="Embeddings") >> embedding
    rag_pipeline >> Edge(label="Data Query") >> vector_database

    aws_cloud >> historic_data
    aws_cloud >> everyday_data

    s3 << historic_data
    s3 << everyday_data

    terminal >> Edge(label="API Call") >> s3
    terminal >> Edge(label="API Call") >> aws_cloud
