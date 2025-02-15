## Project Description
**What is the data science problem to be solved and why is it important?**

* The data science problem to be solved is providing product recommendatiosn to H&M customers.
* Online stores are available to make shopping easier and faster for consumers. Since there are so many choices on the sites, it might be difficult for customers to quickly find what they are looking for. 
* Developing product recommendations will help buyers see the items that they are more likely to purchase. 
* This is important because it could promote sustainability by reducing returns which in turn lessens transportation emissions. 
* By building an effective program, customers could be more likely to shop again at H&M.

## Project Scope
**What data science solutions are we trying to build? What will we deliver, and how will it be used by the client/user?**

* We will be implementing multiple modes of machine learning to create a recommender system for H&M shoppers
  * Association rules
    * Recommendation based off of what has been bought together before
  * Natural language processing techniques using the provided descriptions of the articles 
    * Clustering and find cosine similarity between TFIDF vectors
  * Image processing techniques using the provided images of the articles
  * Using the metrics described below, our recommender system will output 12 recommendations per customer to be evaluated



## Metrics
**How will we quantify the success of the project? What are the common metrics used by others working in the domain?**

* The submissions for this project are evaluated using the Mean Average Precision @ 12.
![image](https://user-images.githubusercontent.com/77793451/216850661-1d05b53e-e55d-452c-ac8c-e039e1e29986.png)
* Using each customer ID in our training data, we will make up to 12 predictions for each one. 
  * These predicted items are for the next 7-day period after the training time period. 
* We will be making predictions for all Customer IDs in our dataset, even if they did not make purchases in the training data. 
* The customers that did not make purchases during the testing period will not be included in the scoring. 
* We will still make 12 predictions for those who ordered less than 12 items, since there is no penalty for doing so.

## Architecture
**What is the nature of the data? What do we expect and how will it be stored/operated on? On what platform would the client/user access any deliverable services (e.g. dashboard) from the project?**

* Data
  * Article metadata
    * 105542 articles in the dataset
    * 23 columns of data:
      * Article_id
      * Product_code
      * Prod_name
      * Product_type_no
      * Product_type_name
      * Product_group_name
      * Graphical_appearance_no
      * Graphical_appearance_name
      * Colour_group_code
      * Colour_group_name
      * Perceived_colour_value_id
      * Perceived_colour_value_name
      * Perceived_colour_master_id
      * Perceived_colour_master_name
      * Department_no
      * Department_name
      * Index_code
      * Index_group_name
      * Section_no
      * Section_name
      * Garment_group_name
      * Garment_group_no
      * Detail_desc
    * Many of the attributes have overlap. For example, graphical_appearance_no provides the same information as graphical_appearance name. The only difference is that graphical_appearance_no is in numerical form.
  * Customer metadata
    * 1371980 customers in the dataset
    * 5 columns of nominal data:
      * FN
      * Active
      * Club_member_status
      * Fashion_news_frequency
      * Postal_code
    * One column of quantitative data (age)
 * Transaction history
    * 31788324 transactions in the dataset
    * Attributes included for each transaction:
      * T_dat
      * Customer_id
      * Article_id
      * Price
      * Sales_channel_id
    * One row = one transaction
    * One customer has many rows
    * Unit of price isn’t of any specific current/unit
  * Article image data
    * 105100 unique images provided
    * 442 articles do not have images
    * Images are organized into folders based on the first three digits of the article_id 
    * Images are in color
    * Image files vary in size from 70 kB to 900 kB with most of the images being between 100 kB and 400 kB.

* Tools
  * Compute GPU (High-Performance Computing)
    * Python 3.8
    * PyTorch singularity container
  * Kaggle notebook
* Dashboard/Presentation
  * Website

## Plan
**Phases (milestones), timeline, short description of what we'll do in each phase. You may consider the phases and deliverables in the course timeline when proposing the plan.**

* Phase 1: Data preprocessing/cleaning, data exploration, and research
  * 2.5 weeks: February 6 - February 22
  * **February 22: Phase 1 Project Demo**
  * Data preprocessing and exploration will be conducted on the customer attributes, product attributes, and purchase history. For example, exploratory data analysis will be performed on product attributes and transaction history to determine which products are frequently purchased and which products haven’t been purchased. The most frequently purchased products will be useful when recommending items to customers who do not have any transaction history since it is impossible to determine what items these customers will like.
  * Different approaches will be researched to decide on two different approaches that will be implemented. Some approaches that were considered include clustering based on the cosine similarity of the product descriptions, matrix factorization, association rules, covisitation matrix, and neural networks on image data. Other methods may be considered if time permits.
  * The implementation for clustering will be started in this phase using TF IDF on the product descriptions and cosine similarity to recommend products that are similar to what customers purchased in the past. 
* Phase 2: Preparing data, clustering, association rules, and further research
  * 5 weeks: February 23 - March 29
  * **March 29: Phase 2 Project Demo**
  * To make the data easier to work with a script will be written to combine the customer data and transaction history data. The combined csv file will contain the customer id along with all of the article ids of the products that that customer purchased. 
  * The evaluation metric will be coded so that the performance of the code can be evaluated without having to produce a submission for all of the customers during each run. Kaggle only accepts submissions that have a recommendation for all of the customers.
  * The implementation for clustering will be completed in this phase.
  * Association rules will also be implemented in this phase.
* Phase 3: Improve model and data visualization
  * 4.5 weeks: March 29 - May 1
  * **May 1: Phase 3 Project + Interactive Dashboard Demo**
  * Research will be conducted during this phase on ways to improve the clustering and association rules models that are already implemented. If there is time left in this phase after improvements are implemented then other approaches can be considered.
  * An interactive dashboard will be created in this phase to provide visuals of insights gained from the data. 

## Personnel
**Who will be working on this project and in what capacities?**

* Team Members
  * Ryan Aclan
  * Salma Hasan
  * Clare Schwarzenberg
* All team members will work on programming, writing reports, and preparing for presentations.


## Communication
**How (platforms, tools, etc.) will we organize communication around the project?**

* Trello
  * Tasks that need to be completed will be added to Trello along with a description of the task under the to do section. Tasks will be tagged as either related to programming, writing reports, or preparing for demos. Different team members will be assigned to each task on Trello. Once tasks are completed they will be moved to the done section. Questions and ideas can also be posted on Trello.
* Weekly Meetings
  * Every Thursday during the lab sessions there is time dedicated to completing project work. During these sessions, team members will update each other on work that has been completed in the last week along with plans for work to be completed for the next week. 
* Group Chat
  * If any meetings outside of class times are needed, they can be scheduled through texting other team members in a group chat. The group chat can also be used for any quick questions or reminders. 
* GitHub
  * Our project will be maintained and collaborated on via GitHub for coding and version control. GitHub will be used to store the data, code, and any important documentation like the project charter. The files will be organized into code, data, and docs folders. GitHub is also used to keep the team up to date on the progress that has been made by each group member because any changes to the project will be committed to GitHub.




