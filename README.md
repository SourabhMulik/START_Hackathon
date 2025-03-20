# START_Hackathon Land Restoration Dashboard Project

## 📌 About the Project
This project is developed for START Hack 2025 as part of the "Innovating for Land Restoration in the Sahel" challenge, sponsored by the United Nations Convention to Combat Desertification (UNCCD) & G20 Global Land Initiative.

## 👥 Team
We are a multidisciplinary team with different backgrounds in Data Science, Management and Digital Business.
Our mission is to combine user-friendly technology that showcases data-driven impact in vulnerable regions like Sahel to enable effective land restoration strategies.

Team Members: Sourabh Mulik, Linh Pham, Jiashuo Han, Sishan Yang

## Overview
**Aims:** explore and address global land restoration challenges

**Region focus:** Sahel region - Assaba 

**Goal:** visualize land cover changes, understand the drivers of vegetation productivity, and identify opportunities for sustainable land management and restoration

**Data:** 
- Provided: https://drive.google.com/drive/folders/1XRiarmgVx5inxudR9K-LM6xpX6IDfiMx?usp=sharing
- External: Soil data from https://soilgrids.org/


## Key Objectives
**Identify Land Cover Trends:** Understand key trends and primary drivers of land cover changes over the past two decades in the Sahel.

**Hotspots of Vegetation Productivity:** Identify hotspots of change in vegetation productivity, considering urban expansion and other influences.

**Integration of Earth Observation Data:** Utilize Earth observation data to address land and water conflicts, identify land degradation, and uncover restoration opportunities.

**Dashboard Solutions:** Develop dashboard solutions to visualize land cover changes and assess their impact on ecosystem health.


## Our Approach
Our approach is data-driven, integrating external observation data and scientific insights. We aim to create a user-friendly, interactive platform that provides actionable insights for stakeholders such as policymakers, funding organization, and local communities.


## Our Methodology
**(Question 1) Identifying Drivers of Land Cover Change:**
- Build regression models to identify significant drivers of land cover change, drivers we selected cover four aspects:
1. Climate - Climate Precipitation
2. Vegetation - GPP (Gross Primary Production)
3. Water - Stream Water Network Data
4. Soil - Soil pH (external data source to enrich the analysis)

**(Question 2) Visualizing Vegetation Productivity and Urban Expansion:**
- Visualize trends in vegetation productivity, identify outliers, and investigate hotspots of change.
- Analyze the impact of urban expansion by visualizing the trend along route networks and population density.

**(Question 3 & 4) Harnessing Data and Technology for Sustainable Management:**

Earth observation data, when combined with scientific insights and technology, helps us see where land and water resources are shrinking and are under pressure. It is done by mapping the drought-prone areas, tracking vegetation loss, or identifying overused grazing lands. This makes it easier for governments and communities to act early, avoid conflicts, and protect vital resources.
Technology like satellite-based dashboards or mobile apps can empower local communities by giving them easy access to the information about their own land in very easy understandable way using maps, graphs, and trend lines. This information shows where the forests are shrinking, urban areas are growing, or vegetation is declining and where restoration is possible or where any efforts in farming might fail. This creates transparency, builds trust, and encourages people to take part in sustainable land management.
This combined approach creates a scalable model for global initiatives like the G20 Land Restoration Initiative by providing a framework that can be copied in other regions facing similar land degradation and resource conflicts, turning data into real action on the ground. This also helps stakeholders like the governments, NGOs, local leaders to quickly assess where intervention is needed for rehabilitation or resource management.


## Methodology Used Thus Far
**Data Preperation:**
We have extracted and projected the provided Earth observation data, and we also plan to process external data.
**Modeling:** 
Tool: python
A naive regression model is being used to identify significant drivers of land cover changes, with the inclusion of external datasets for more comprehensive analysis.
**Visualization:** 
Tool: figma
Preliminary visualizations of vegetation productivity trends and urban expansion are in progress, focusing on identifying key hotspots of change.


## Final Product
The final product is an interactive dashboard that empowers stakeholders to visualize, analyze, and make decisions based on factors affecting the land cover. The dashboard includes customizable analytical tools, sensitivity analysis, various level of detailed profiles, and visualizations to aid in the restoration and conservation of land, especially in the Sahel region.


## Project Milestones
**Mid-Project Submission (20th March):** Submit a one-pager or PPT summarizing approach, expected outcomes, and methodology.
**Final Submission:** Deliver a fully functional dashboard with analytical tools and district-level profiles, ready for stakeholders to use.


