pipeline{
  agent any
  stages{
    stage('Checkout'){
      steps{
        echo'Cloning Github Repo'
      }
    }
    stage('Build'){
      steps{
        echo'Building Flask App'
      }
    }
    stage('Test'){
      steps{
        echo 'Running Tests...'
      }
    }
    stage('Deploy'){
      steps{
        echo'Deploying Application'
      }
    }
  }
}
