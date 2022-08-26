<template>
  <div class="input-wrapper">
    <SearchIcon class="icon" />
    <input class="input" placeholder="Type to search"/>
  </div>
</template>

<script>
import SearchIcon from '@components/icons/SearchIcon'

export default {
  name: 'BaseInput',
  components: {
    SearchIcon
  }
}
</script>

<style scoped>
  .input-wrapper {
    position: relative;

    display: flex;
    align-items: center;

    height: 40px;
  }

  .input {
    width: 262px;
    height: 40px;
    padding-left: 32px;

    border: 1px solid #2D2D31;
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    outline: none;
    color: var(--primary-text-color);
    background-color: var(--secondary-bg-color);
  }

  .input::placeholder {
    color: var(--secondary-text-color);
  }

  .icon {
    position: absolute;
    left: 10px;

    width: 16px;
    height: 16px;
  }
</style>
