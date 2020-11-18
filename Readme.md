
# Plant disease detection

Plant disease is one of the main problems in the agriculture since they cause great damages to agriculture crops by significantly decreasing production. It is then essential to have powerful early dignoses to prevent such losses,the solution proposed in this work was based on CNN (Convolution Neural Network ), which was widely used the last years in the classification tasks for their accurate results in production.<br>

 
# Dataset

This <a href="https://www.kaggle.com/saroz014/plant-diseases">dataset</a> was used to train and evaluate the model.<br>


# training 

the training and evaluating steps was done using Keras,I took also advantage of the transfer learning technique for a faster training (architecture used : <a href="https://keras.io/applications/#vgg16">VGG16</a>).<br>

Here is the <a href="https://drive.google.com/file/d/1-K-ZwprY9CjkqD_dtlm9Q0SOTLpH2fh_/view">link</a> to the final checkpoint ( trained weights ). 

# requirements
```
pip install -r requirements.txt

```  