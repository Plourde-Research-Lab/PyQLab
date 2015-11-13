'use strict';

var expSettingsApp = angular.module('expSettingsApp', ['ngRoute', 'ui.router', 'ui.bootstrap']);

expSettingsApp.config(['$stateProvider', '$locationProvider',
    function($stateProvider, $locationProvider) {
    $stateProvider
        .state('root',{
        	views: {
        		'channels': {
        			templateUrl: 'views/channels.html',
        			controller: expSettingsApp.mainCtrl
        		},
                'physicalChannels@root': {
                    templateUrl: 'views/channelViews/physicalChannelViews.html',
                    controller: expSettingsApp.mainCtrl
                },
                'logicalChannels@root': {
                    templateUrl: 'views/channelViews/logicalChannelViews.html',
                    controller: expSettingsApp.mainCtrl
                },
        		'instruments': {
        			templateUrl: 'views/instruments.html',
        			controller: expSettingsApp.mainCtrl
        		},
        		'measurements': {
        			templateUrl: 'views/measurements.html',
        			controller: expSettingsApp.mainCtrl
        		},
        		'sweeps': {
        			templateUrl: 'views/sweeps.html',
        			controller: expSettingsApp.mainCtrl
        		}
        	}
        })
		// .state('channels', {
		// 	templateUrl: 'views/channels.html',
		// 	controller: expSettingsApp.mainCtrl
		// })
		// .state('channels.physicalQuadrature', {
		// 	templateUrl: 'views/channelViews/physicalQuadratureChannelViews.html'
		// })

    $locationProvider.html5Mode(true);
}]);
