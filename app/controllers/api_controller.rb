class ApiController < ApplicationController
  def all_stages
    @stages = Stage.find(:all, :conditions => "latitude IS NOT NULL", :select => "name, latitude, longitude, id")
    respond_to do |format|
      format.json { render :json => @stages.to_json }
    end
  end
end
