<template>
  <div class="project-cart-wrapper transition" @click="openWorkspace">
    <div class="project-title-wrapper">
      <div class="title">{{ title }}</div>

      <PointsIcon @click="openModal" class="points-icon" />
    </div>

    <div class="cart-button-wrapper">
      <div class="cart-image-wrapper">
        <img
          v-for="(item, index) in members.slice(0, 4)"
          :key="'photo' + index"
          :src="item?.user_profile.photo"
          :style="`z-index=${index + 1}`"
          class="cart-image"
        />

        <div v-if="members.length > 4" class="members-count">
          +{{ members.length - 4 }}
        </div>
      </div>

      <button
        :style="`z-index=${members.length + 1}`"
        class="new-project"
        @click="addNewProject"
      >
        <span class="button-text">new</span>
        <span class="circle" aria-hidden="true"><PlusIcon /></span>
      </button>
    </div>
  </div>
</template>

<script>
import PlusIcon from '@components/icons/PlusIcon'
import PointsIcon from '@components/icons/PointsIcon'

export default {
  name: 'ProjectItem',
  components: {
    PointsIcon,
    PlusIcon,
  },
  props: {
    title: {
      type: String,
      default: '',
    },
    id: {
      type: Number,
      required: true,
    },
    members: {
      type: [Array, Object],
      required: true,
    },
  },
  methods: {
    openWorkspace() {
      this.$emit('navigate-to-workspace')
    },
    addNewProject() {
      this.$emit('add-new-project')
      event.stopPropagation()
    },
    openModal() {
      this.$emit('open-modal', this.id)
      event.stopPropagation()
    },
  },
}
</script>

<style lang="scss" scoped>
.project-cart-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-shrink: 1;

  width: calc((100% / 5) - (4rem / 5));
  height: 130px;
  padding: 16px 21px 13px 18px;

  border: 1px solid #2d2d31;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

  cursor: pointer;

  background: linear-gradient(to left, rgba(5, 95, 252, 0.7), #242529, #242529);
  background-size: 200%;
  transition: 0.5s;

  &:hover {
    background-position: right;
  }
}

.project-title-wrapper {
  display: flex;
  justify-content: space-between;

  color: var(--primary-text-color);
}

.title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 22px;
}

.cart-button-wrapper {
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-image-wrapper {
  position: relative;

  display: flex;

  .cart-image {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-grow: 0;
    flex-shrink: 0;

    width: 22px;
    height: 22px;

    border-radius: 100%;
    border: 1px solid var(--secondary-text-color);

    background-color: white;

    font-size: 10px;

    &:not(:first-child) {
      margin-left: -10px;
    }
  }

  .members-count {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    flex-grow: 0;

    width: 22px;
    height: 22px;
    margin-left: 8px;

    border-radius: 100%;
    border: 1px dashed var(--secondary-text-color);

    color: var(--secondary-text-color);

    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
  }
}

.new-project {
  position: absolute;
  right: 0;

  width: 74px;
  height: 30px;
}

.points-icon {
  pointer-events: stroke;

  flex-shrink: 0;

  color: var(--secondary-text-color);

  transition: all 0.3s;
  z-index: 3;
}

.points-icon:hover {
  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--primary-button-color);
}

button {
  position: relative;

  display: flex;
  align-items: flex-end;
  justify-content: flex-end;

  padding: 0;

  border: 0;
  background: transparent;

  font-size: inherit;
  font-family: inherit;

  cursor: pointer;
  outline: none;
  vertical-align: middle;
  text-decoration: none;
  transition: 3s;
}

button.new-project .circle {
  position: relative;

  display: flex;
  align-items: center;

  padding: 0 5px 0 9px;
  margin: 0;
  width: 32px;
  height: 30px;

  background: var(--icon-bg-color);
  border-radius: 1.625rem;

  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
}

button.new-project .button-text {
  position: absolute;
  top: 50%;
  left: 60%;
  transform: translate(-50%, -50%);

  text-align: center;

  opacity: 0;
  z-index: 2;
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
}

button:hover .circle {
  width: 100%;
  background: var(--primary-button-color);
}

button:hover .button-text {
  opacity: 1;
  color: var(--primary-text-color);
}

@media screen and (max-width: 1080px) {
  .project-cart-wrapper {
    width: calc((100% / 4) - (3rem / 4));
  }
}

@media screen and (max-width: 750px) {
  .project-cart-wrapper {
    width: calc((100% / 2) - (2rem / 3));
    height: 160px;
  }
}
</style>
