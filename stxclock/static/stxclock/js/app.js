$(function() {
  // The View Model
  var viewModel = {
    init: function() {
      view.init();
    }
  };

  // The View
  var view = {
    init: function() {
      this.currentUTCTime();
      this.render();
    },

    // Adds the current UTC time to the top of the page
    render: function() {
      $('#utctime').append('<p>' + "Current UTC Time: " + view.currentUTCTime() + '</p>');
      this.timeLoop();
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
