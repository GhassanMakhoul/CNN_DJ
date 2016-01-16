# CNN_DJ
Using convolutional neural networks in Python to classify music and ultimately recommend songs based on latent representations

This is an educational endeavor into applying Convolutional Neural Networks to learn features of music. 
This  project is currently under the earliest phases of construction, which means much of the code is subject to the 
tides of change. So, I will provide a list of goals we hope to accomplish.

1. Handle audio data and create representations of songs that can easily be passed into a CNN.
  As of today our approach consists of converting these audio signals into mel-spectrograms using 
  audio signal processing API's
2. Train a simple CNN with 2 convolutional layers each followed by maxpooling/downsampling layers
  and one fully connected layer on our training set.
3. Eventually we wish to separate data features such as, genre, tempo, even key. But this is a long term goal
  Right now it would be great just to have a neural net up and running
4. Speed up  the neural net using distributed computing API. We intend to use spark for vectorization in this phase.
5. Experiment with other CNN structures for more sophisticated classification. 

Being a full time student, a lot of this is very new to me. This will be my first Neural Net outside of the classroom/project setting.
In addition, this is a learning project for me, mainly for the signal processing portion.

Feel free to contact me at ghassanmakhoul@berkeley.edu!
