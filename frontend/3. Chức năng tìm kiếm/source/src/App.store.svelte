<script>
  import { counter } from "./stores";
  
  function increase() {
    counter.update(val => val+1);
  }

  function decrease() {
    counter.update(val => val-1);
  }
  let counterValue;

  counter.subscribe(val => counterValue = val);
</script>

<main>
	<div class="container mt-3">
		Counter: {counterValue} 
      {" "}

      <button 
        class="btn btn-sm btn-primary" 
        on:click={increase}
      >+</button>

      {" "}
      
      <button 
        class="btn btn-sm btn-danger" 
        on:click={decrease}
      >-</button>
	</div>
</main>