<img src="pink_logo.png" width="300" ><img> 

# RoboCupido                

Match making system based on people's likes, using the K-means machine learning algorithm.

## Project Details

This project is made using [scikit-learn](https://scikit-learn.org/stable/) with [pandas](https://pandas.pydata.org/). For data preprocessing and management we also used [Jupyter](https://jupyter.org/) and [R language](https://www.r-project.org/about.html).

### Development team

| Name                    | Email                                                               | Github                                                       | Role      |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| Aurora Tijerina Berzosa | [auro.tj@gmail.com](mailto:auro.tj@gmail.com)                       | [@AuroTB](https://github.com/aurotb)                         | Matchmaking algorithm |
| José Francisco Pacheco Quintana  | [pacocheco7@gmail.com](mailto:pacocheco7@gmail.com)         | [@JFPach98](https://github.com/JFPach98)                   | Data preprocessing |
| Brenda Guadalupe Martínez Orta | [bmaor2001@gmail.com](mailto:bmaor2001@gmail.com)               | [@bmaor2001](https://github.com/bmaor2001)                       | Result data decoding |
| José Alfonso Cisneros   | [joseacisnerosm@gmail.com](mailto:joseacisnerosm@gmail.com)         | [@Josecisneros001](https://github.com/Josecisneros001)       | Mail automatization |

## Project setup

1. Clone the project repository on your local machine.

   SSH:

   ```bash
   $ git clone https://github.com/RoBorregos/RoboCupido.git
   ```

2. You can install all requirements by running:

    ```bash
    $ pip3 install -r requirements.txt
    ```

### Running the matchmaking algorithm

To run the matchmaking algorithm make sure binarized.csv data file is inside ```data/```, then run:

```bash
$ python matchingModel.py
```

When finished, results should be saved in ```resuls/``` folder.

## Resources
You can check out this usefull K-means tutorials:
- https://realpython.com/k-means-clustering-python/
- https://www.aprendemachinelearning.com/k-means-en-python-paso-a-paso/
