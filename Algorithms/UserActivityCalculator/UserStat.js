//About: This Script updates the server after every "SEND_TO_SERVER_DURATION" seconds. It displays LogOut warning when
//user is idle and "PageTimeOutWarning" seconds is left to log out. It finally logs out after "PageTimeout" seconds.

        //Time to send to the server in seconds --> Please update the values
        var PageTimeout = 15
        var PageTimeOutWarning = 10
		var SEND_TO_SERVER_DURATION = 5
		TimeMe.initialize({
			currentPageName: "timeCalc", // current page
			idleTimeoutInSeconds: 5, // stop recording time due to inactivity after 10 minutes
		});

		TimeMe.callAfterTimeElapsedInSeconds(4, function () {
			console.log("The user has been using the page for 4 seconds! Let's prompt them with something.");
		});

		TimeMe.callAfterTimeElapsedInSeconds(9, function () {
			console.log("The user has been using the page for 9 seconds! Let's prompt them with something.");
		});


		window.onload = function () {
			TimeMe.trackTimeOnElement('area-of-interest-1');
			TimeMe.trackTimeOnElement('area-of-interest-2');

			//Calculate Idle Time
			idle = PageTimeout
			pingCounter = 0

			var elapsed = setInterval(function () {
				//If the idle time exceeds certain Threshold, Send information to Server & stop the timer
				let timeSpentOnPage = TimeMe.getTimeOnCurrentPageInSeconds();
				if(idle <= 0){
                    document.getElementById('LogWarn').textContent = "Logged Out";
					console.log("Logout and send time to server " + timeSpentOnPage / 3600.0 + " Hours")
					stopElapsedTime()
                }
                else if(idle <= PageTimeOutWarning){
                    document.getElementById('LogWarn').textContent = "Please interact. Otherwise you will log out in " + idle + " seconds.";
                }

				if(pingCounter == SEND_TO_SERVER_DURATION){
					console.log("Update time on Server")
					pingCounter = 0
				}
				pingCounter += 1
				document.getElementById('timeInSeconds').textContent = timeSpentOnPage.toFixed(2);
				if (TimeMe.isUserCurrentlyOnPage && TimeMe.isUserCurrentlyIdle === false) {
					idle = PageTimeout
					document.getElementById('activityStatus').textContent = "You are actively using this page."
				} else {
					//Send updated time to the server
					//Format: {"time-elapsed": _____, "day": new Date()}
					idle -= 1
					document.getElementById('activityStatus').textContent = "You have left the page."
				}
				let timeSpentOnElement = TimeMe.getTimeOnElementInSeconds('area-of-interest-1');
				document.getElementById('area-of-interest-time-1').textContent = timeSpentOnElement.toFixed(2);

				let timeSpentOnElement2 = TimeMe.getTimeOnElementInSeconds('area-of-interest-2');
				document.getElementById('area-of-interest-time-2').textContent = timeSpentOnElement2.toFixed(2);

			}, 1000);

			function stopElapsedTime() {
				TimeMe.stopAllTimers()
				clearInterval(elapsed);
			}
        }
        
//Created by: Prakshal Jain (prakshal@buffalo.edu)
//Libraries Used: https://github.com/jasonzissman/TimeMe.js/