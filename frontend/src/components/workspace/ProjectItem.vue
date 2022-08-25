<template>
  <div class="project-cart-wrapper">
    <div class="project-title-wrapper">
      <div class="title">South Arabia and India and smthng</div>

      <div><PointsIcon/></div>
    </div>

    <div class="cart-button-wrapper">
      <div class="test-user">User</div>

      <button class="icon-btn add-btn">
        <PlusIcon class="plus-icon" />
        <div class="btn-txt">New</div>
      </button>
    </div>
  </div>
</template>

<script>
import PointsIcon from '../icons/PointsIcon'
import PlusIcon from '../icons/PlusIcon'

export default {
  name: "ProjectItem",
  components: {
    PointsIcon, PlusIcon
  }
}
</script>

<style scoped>
.project-cart-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 230px;
  height: 130px;
  padding: 16px 21px 13px 18px;

  border: 1px solid #2D2D31;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

  cursor: pointer;
  background: var(--secondary-bg-color);
}

.project-title-wrapper {
  display: flex;

  color: var(--primary-text-color);
}

.title {
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 22px;
}

.cart-button-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.test-user {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 22px;
  height: 22px;

  border-radius: 100%;

  background-color: red;

  font-size: 10px;
}

.icon-btn {
  width: 30px;
  height: 30px;
  background: var(--primary-bg-color);
  border-radius: 25px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  font-weight: 500;
  font-family: inherit;
}

.plus-icon {
  position: absolute;
  top:50%;
  left:50%;
  transform:translate(-50%, -50%);
}

.add-btn:hover {
  width: 120px;
}

.add-btn:hover .plus-icon {
  position: absolute;
  top:50%;
  left:15%;
  transform:translate(-50%, -50%);
}

.btn-txt {
  opacity: 0;
}

.add-btn:hover .btn-txt {
  opacity: 1;
}
</style>
