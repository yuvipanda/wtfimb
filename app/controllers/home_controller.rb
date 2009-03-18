class HomeController < ApplicationController
  def index
    @title = 'Home'
    @onload = 'init();'
  end
end
