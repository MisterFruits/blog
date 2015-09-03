% rebase('base.tpl', title='Upload to mad-dam')
<form action="/mad-dam" method="post" enctype="multipart/form-data">
  <div class="form-group">
    <label for="title">Title</label>
    <input type="text" class="form-control" id="title" name="title">
  </div>
  <div class="form-group">
    <label for="caption">Caption</label>
    <input type="text" class="form-control" id="caption" name="caption">
  </div>
  <div class="form-group">
    <label for="inputImage">File input</label>
    <input type="file" id="inputImage" accept="image/*" name="upload">
    <p class="help-block">Image only here.</p>
  </div>
  <button type="submit" class="btn btn-primary">Upload to mad-dam</button>
</form>

