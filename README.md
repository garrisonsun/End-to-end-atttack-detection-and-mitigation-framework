<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">End-to-end Attack Detection and Mitigation Framework</h1>
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
    <li><a href="#simulation">Simulation</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#cite-this-work">Cite this work</a></li>
    <li><a href="#license">License</a></li>
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
3. Install [Gambit](https://gambitproject.readthedocs.io/en/latest/build.html) Python extention 
  
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

## Authors
- [Guoxin Sun](https://electrical.eng.unimelb.edu.au/people/research-students)

- [Tansu Alpcan](https://findanexpert.unimelb.edu.au/profile/425318-tansu-alpcan)

- [Ben Rubinstein](https://findanexpert.unimelb.edu.au/profile/20074-ben-rubinstein)
  
- [Seyit Camtepe](https://people.csiro.au/C/S/Seyit-Camtepe)

## Cite this work
If you find this work useful, please consider to cite the following reference [paper](https://garrisonsun.github.io/End-to-end-atttack-detection-and-mitigation-framework/):
```
@inproceedings{guoxin2021strategic,
  title={Strategic mitigation against wireless attacks onautonomous platoons.},
  author={Sun, Guoxin and Alpcan, Tansu and Rubinstein, Benjamin and Camtepe, Seyit},
  booktitle={ECML/PKDD},
  pages={--},
  year={2021}
}
```
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

