var myApp = angular.module('CreateTaskApp', []);

myApp.controller("CreateTaskController",function($scope, $http)
 {
   $scope.happy = "hello";
   $scope.createTask = function(task){
     var config = {
             headers : {
                 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                 }
             }

     var post_url = '/tasks/api/' ;
     $http.put(post_url,
                 "done="+encodeURIComponent('N') +
                 "&title="+encodeURIComponent(task.title) +
                 "&description="+encodeURIComponent(task.description),

                  config
                ).success(function(response){
                 console.log(response);
                 $scope.SuccessMessage = "Task created";
                 $scope.task.title ="";
                 $scope.task.description="";
                 },function errorCallback(response) {
                     console.log(response);
                 });
   }

 });

var myApp = angular.module('TaskApp', []);

myApp.controller("MyController",function($scope, $http)
 {
   $http.get('/tasks/api/?format=json').success(function(response){

   $scope.tasks = response;

    // Update model
    angular.forEach($scope.tasks, function(task) {
      task.checked = task.done == 'Y'? 1 :0;
      if (task.checked) {
        task.myClass ="strikethrough";
      }

      });

    $scope.updateTask = function(task){


      elm =  document.querySelector( '#tasklist' + task.id  )
      if(elm.classList.contains('strikethrough')){
        angular.element(elm).removeClass('strikethrough');
      }
      else{
        angular.element(elm).addClass('strikethrough');
      }
        task.done = task.checked ? 'N' : 'Y';
        var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                    }
                }
        var post_url = '/tasks/api/' + task.id + '/';
        $http.put(post_url,
                    "done="+encodeURIComponent(task.done) +
                    "&title="+encodeURIComponent(task.title) +
                    "&description="+encodeURIComponent(task.description),

                     config
                   ).success(function(response){
                    console.log(response);
                    },function errorCallback(response) {
                        console.log(response);
                    });
        task.myClass = task.checked ? "strikethrough" : "";
        };

    });
 });
