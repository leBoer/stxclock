$(function() {
  //**---The View Model---**\\
  var viewModel = {
    init: function() {
      view.init();
      var csrftoken = this.getCookie('csrftoken');
    },
    getExchanges: function() {
      $.ajax({
        url: 'api/exchanges',
        success: function(data) {
          console.log('AJAX was a success!');
        }
      }).done(function (data) {
        view.renderExchanges(data);
      })
    },
    getCookie: function(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  };

  //**---The View---**\\
  var view = {
    init: function() {
      this.currentUTCTime();
      this.render();
    },

    // Adds the current UTC time to the top of the page
    render: function() {
      $('#utctime').append('<p>' + "Current UTC Time: " + view.currentUTCTime() + '</p>');
      viewModel.getExchanges();
      this.timeLoop();
    },
    // Rendering function just for the AJAX stuff
    renderExchanges: function(data) {
      var exchanges = data.results;
      console.log(exchanges);
    },

    // Gets the current UTC time
    currentUTCTime: function() {
      var d = new Date();
      return d.toUTCString();
      },

    // Keeps the times updated
    timeLoop: function() {
      setInterval(view.updateTime, 1000);
    },

    // Updates the current UTC (and local time when that is implemented)
    updateTime: function() {
      $('#utctime').text('');
      $('#utctime').append('<p>' + "Current UTC Time: " + view.currentUTCTime() + '</p>');
    }
  };
  viewModel.init();
});
