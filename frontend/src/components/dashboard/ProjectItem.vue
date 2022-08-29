<template>
  <div class="project-cart-wrapper">
    <div class="project-title-wrapper">
      <div class="title">South Arabia and India and smthng</div>

      <PointsIcon class="points-icon" />
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
import PlusIcon from '@components/icons/PlusIcon'
import PointsIcon from '@components/icons/PointsIcon'

export default {
  name: "ProjectItem",
  components: {
    PointsIcon, PlusIcon
  }
}
</script>

<style lang="scss" scoped>
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

  background-color: var(--secondary-bg-color);
  cursor: pointer;

  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
  &:hover {
    background: linear-gradient(140deg, rgba(45,45,49,1) 30%, rgba(5,68,179,1) 78%);
  }
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

  background-color: white;

  font-size: 10px;
}

.points-icon {
  flex-shrink: 0;

  color: var(--secondary-text-color);

  transition: all 0.3s;
}

.points-icon:hover {
  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--primary-button-color);
}

.icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 30px;
  height: 30px;

  border: none;
  border-radius: 100%;

  background-color: var(--icon-bg-color);

  cursor: pointer;
  transition: all 0.5s;
}

.btn-txt {
  display: none;
}

.icon-btn:hover {
  width: 74px;

  border-radius: 15px;

  background-color: var(--primary-button-color);

  .btn-txt {
    display: block;

    margin-left: 8px;

    color: var(--primary-text-color);
  }
}
</style>
