<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">End-to-end Attack Detection and Mitigation Framework</h3>
<p align="center">
  
  <details open="open">
  <summary>Table of Contents</summary>
  <ol>
      <li><a href="#about-the-project">About The Project</a></li>
      <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#examples">Examples</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#simulation">Simulation</a></li>
   </ol> 
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
We apply game theory, control theory and advances of machine learning to improve the robustness of vehicle platoons with an end-to-end attack detection and mitigation framework. In this project, we demenstrate the core algorithms.  

<!-- GETTING STARTED -->
## Getting Started

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/garrisonsun/End-to-end-atttack-detection-and-mitigation-framework.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage
   
  ```sh
  python NumericalExample.py <options>
  ```
## Examples
  ```
  (1) python NumericalExample.py
      - returns the Player' payoffs, prob. of initiating an attack 
        and prob. of defloying acc for defending 
  (2) python NumericalExample.py -p
      - starts to type in utility values and detector properties
    
       [-h] [-p]

  optional arguments:
    -h, --help        show this help message and exit
    -p, --parameters  Inputs utility values and detector properties.
  ```  
  
## Simulation

https://user-images.githubusercontent.com/50089203/123204755-112de680-d4fc-11eb-985c-2a0df8add4ee.mp4

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

