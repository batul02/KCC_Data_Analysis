# Hadoop and Natural Language Processing Based Analysis on Kisan Call Center (KCC) Data

**Index**

1. Abstract 
   1. Problem Statement 
   1. Objective 
   1. Data Description 
1. Why is it a Big data problem? 
1. Big Data Tools   
1. Implementation 
   1. Code 
   1. Commands 
   1. Execution 
1. Conclusion 

**Abstract**

- **Problem Statement** 

  The Kisan Call Center (KCC) accumulates a vast amount of data related to farmer queries, encompassing various agricultural domains. Analyzing this data presents a significant challenge due to its volume, velocity, and variety. 

- **Objective** 

  This project aims to utilize Hadoop and Natural Language Processing (NLP) techniques to analyze the KCC data effectively. Specifically, the focus is on understanding the queries posed by farmers, identifying patterns, and providing insights to improve agricultural practices and farmer support services. 

- **Data Description** 

  The dataset used for analysis in this report is a CSV file with a size of approximately 6.7GB. It comprises several columns containing information related to queries received by the Kisan Call Center (KCC). 

  The dataset is available[ here.](https://kcc-chakshu.icar.gov.in/insights.html) 

**Why is it a Big Data Problem?**

- **Volume**: The dataset under analysis is vast, comprising numerous farmer queries directed to the Kisan Call Center (KCC). Each query represents a distinct interaction, contributing to a substantial volume of data that necessitates thorough processing and analysis. 
- **Variety**: The dataset exhibits diversity, encompassing a wide range of agricultural queries covering topics such as crop issues, pest management, fertilizer usage, and disease identification. Queries may vary significantly in language, dialect, and specific agricultural context, resulting in diverse textual data. 
- **Velocity**: Data generation occurs rapidly and continuously as farmers seek assistance and information from the KCC regarding their agricultural concerns. This constant influx of queries demands real-time or near-real-time processing and analysis to provide timely insights and responses to farmers. 
- **Veracity**: The dataset may contain inconsistencies, errors, or noise stemming from factors like human data entry errors, variations in farmers' language or terminology, and technical glitches during data collection. Ensuring data accuracy and reliability is crucial for obtaining meaningful insights and making informed decisions. 
- **Value**: Despite challenges posed by the dataset's volume, variety, velocity, and veracity, deriving insights from the KCC dataset can yield significant value. Analysis of queries and trends can provide valuable insights into farmers' needs, challenges, and preferences, informing decision-making processes, enhancing agricultural practices, and improving support services for farmers. Ultimately, this can lead to increased agricultural productivity, sustainability, and welfare. 

**Big Data Tools**

The paper combines MapReduce in a Hadoop environment and Natural Language Processing (NLP) clustering in PySpark for data analysis: 

1. MapReduce in Hadoop: 
- Tasks: 
  - Frequency of Crops Asked About 
  - Frequency of Query Types 
  - Frequency of Crop Categories 
  - Frequency of Different Sectors 
- Approach: 
- MapReduce distributes tasks across nodes for parallel processing. 
- Mapping phase extracts relevant information from each record. 
- Reducing phase aggregates and computes frequencies. 
2. NLP Clustering in PySpark: 
- Task: Grouping Similar Queries 
- Approach: 
- Data pre-processing for noise removal, case folding, and lemmatization. 
- Feature matrix creation with unique words (unigrams) and query frequencies. 
- Similarity matrix generation based on word frequency. 
- Clustering using DBSCAN for cluster estimation and agglomerative clustering for grouping queries.

**Implementation**

- There are 4 Map-Reduce task:
- Implement all the 4 task using given steps bleow: 

  **Step1:** 

  Starting the Hadoop env by using : ./start-all.sh 

  **Step2:** 

  Insert all the required file i.e. data file, code file using put command: 

  hdfs dfs -put -f /mnt/d/batul/Sem2/bd/project/query\_grouping.py /code/query\_grouping.py 

  **Step3:** 

  Executing command for python file: 

  As we are running python code for map reduce, in python we don’t need to create jar file but we can run our python code directly.  


**Step4**: 

See the output by command: hdfs dfs -cat /output1/part-00000 


- NLP Query Clustering PySpark Task :
- PySpark is the Python API for Apache Spark, a fast and general- purpose cluster computing system. It provides high-level APIs in Python, Java, Scala, and R, making it easier to build parallel applications to process large-scale data sets. 

  **Importance of PySpark for the Task:** 

- Distributed Computing: PySpark enables the processing of large-scale datasets by distributing computations across a cluster of machines. 
- Parallelism: It leverages parallel processing to perform operations in-memory, leading to faster processing of data. 
- Scalability: PySpark can scale horizontally by adding more nodes to the cluster, allowing it to handle growing volumes of data. 
- Ease of Use: PySpark provides high-level APIs and libraries for data processing, machine learning, and streaming analytics, making it accessible to data scientists and engineers. 
- Integration: It seamlessly integrates with other big data technologies like Hadoop, HDFS, Hive, and HBase, enabling interoperability with existing data infrastructures. 

**Summary of the Code**: 

I use PySpark for preprocessing textual data, performing NLP-based clustering, and visualizing the results. It loads a dataset of farmer queries, preprocesses the text using tokenization and lemmatization, transforms it into TF-IDF vectors, and clusters similar queries using the KMeans algorithm. Finally, it visualizes the clustering results to gain insights into the queries received by the Kisan Call Center. PySpark's distributed computing capabilities make it well-suited for processing large volumes of textual data and performing complex analytics tasks efficiently. 


**Conclusion**: 

- In conclusion, the analysis of Kisan Call Center (KCC) data using big data and natural language processing (NLP) techniques has provided valuable insights into the queries raised by farmers.  
- Through the application of MapReduce in Hadoop environment, we were able to perform various tasks such as determining the frequency of different crops, query types, crop categories, and sectors. This allowed us to understand the prevalent concerns and topics of interest among farmers. 
- Additionally, by leveraging PySpark, we conducted NLP-based clustering to group similar queries. This approach helped identify common themes and questions asked by farmers, enabling more efficient handling of queries and provision of relevant information through KCC. 
- Overall, the combination of big data analytics and NLP techniques offers significant potential for enhancing the effectiveness and responsiveness of agricultural support systems like KCC. By gaining deeper insights into farmer queries and concerns, agricultural authorities can better tailor their services and interventions to meet the needs of farmers, ultimately contributing to improved agricultural productivity and livelihoods. 

